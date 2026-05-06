import logging
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from app.payment import indirim_hesapla, odeme_yap
from flask_sqlalchemy import SQLAlchemy

# 1. Flask Uygulamasını Tanımla
app = Flask(__name__)

# 2. Loglama Ayarları
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='megamarket.log',
    filemode='a'
)

# 3. Veritabanı Ayarları
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 4. Veritabanı Modeli
class Islem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    toplam_tutar = db.Column(db.Float, nullable=False)
    indirim_orani = db.Column(db.Float, nullable=False)
    odenecek_tutar = db.Column(db.Float, nullable=False)
    # Varsayılan değeri yerel saate (datetime.now) çektik
    tarih = db.Column(db.DateTime, default=datetime.now)

# Veritabanını oluştur
with app.app_context():
    db.create_all()

@app.route('/')
deef home():
    return render_template('index.html')

@app.route('/indirim', methods=['POST'])
def api_indirim():
    data = request.get_json()
    logging.info(f"İndirim isteği alındı: {data}")
    
    try:
        toplam = data['toplam_tutar']
        oran = data['indirim_orani']
        sonuc = indirim_hesapla(toplam, oran)
        
        # VERİTABANINA KAYIT
        yeni_islem = Islem(
            toplam_tutar=toplam,
            indirim_orani=oran,
            odenecek_tutar=sonuc
        )
        db.session.add(yeni_islem)
        db.session.commit()

        logging.info(f"Hesaplama ve kayıt başarılı. Sonuç: {sonuc}")
        return jsonify({"yeni_tutar": sonuc, "durum": "basarili"}), 200
    except Exception as e:
        logging.error(f"Hata oluştu: {str(e)}")
        return jsonify({"hata": str(e), "durum": "basarisiz"}), 400

@app.route('/gecmis')
def gecmis_getir():
    # En son yapılan işlemi en üstte göstermek için tarihe göre azalan sıraladık
    islemler = Islem.query.order_by(Islem.tarih.desc()).all()
    liste = []
    for i in islemler:
        liste.append({
            "tutar": i.toplam_tutar,
            "oran": i.indirim_orani,
            "sonuc": i.odenecek_tutar,
            # JS tarafında kolayca formatlayabilmek için ISO formatında gönderiyoruz
            "tarih": i.tarih.isoformat() 
        })
    return jsonify(liste)

@app.route('/odeme', methods=['POST'])
def api_odeme():
    data = request.get_json()
    try:
        sonuc = odeme_yap(data['bakiye'], data['odenecek_tutar'])
        return jsonify({"kalan_bakiye": sonuc, "durum": "basarili"}), 200
    except Exception as e:
        return jsonify({"hata": str(e), "durum": "basarisiz"}), 400

if __name__ == '__main__':
    app.run(debug=True)