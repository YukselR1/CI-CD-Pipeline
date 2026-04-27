# app/main.py
import logging

# Loglama Ayarları: İşlemleri 'megamarket.log' dosyasına tarihle kaydet
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='megamarket.log',
    filemode='a' # 'a' (append) modu üzerine ekleyerek devam eder
)

from flask import Flask, request, jsonify, render_template
from app.payment import indirim_hesapla, odeme_yap

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/indirim', methods=['POST'])
def api_indirim():
    data = request.get_json()
    logging.info(f"İndirim isteği alındı: {data}") # İstek günlüğü
    
    try:
        sonuc = indirim_hesapla(data['toplam_tutar'], data['indirim_orani'])
        logging.info(f"Hesaplama başarılı. Sonuç: {sonuc}") # Başarı günlüğü
        return jsonify({"yeni_tutar": sonuc, "durum": "basarili"}), 200
    except Exception as e:
        logging.error(f"Hesaplama sırasında hata oluştu: {str(e)}") # Hata günlüğü
        return jsonify({"hata": str(e), "durum": "basarisiz"}), 400

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