# app/main.py
from flask import Flask, request, jsonify
from app.payment import indirim_hesapla, odeme_yap

app = Flask(__name__)

@app.route('/indirim', methods=['POST'])
def api_indirim():
    data = request.get_json()
    try:
        sonuc = indirim_hesapla(data['toplam_tutar'], data['indirim_orani'])
        return jsonify({"yeni_tutar": sonuc, "durum": "basarili"}), 200
    except Exception as e:
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