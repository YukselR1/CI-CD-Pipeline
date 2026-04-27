# 🛒 MegaMarket Full-Stack Gateway

MegaMarket projesinin ödeme ve indirim süreçlerini yöneten, modern bir web arayüzüne sahip ve **CI/CD (Sürekli Entegrasyon)** odaklı geliştirilmiş profesyonel bir yazılım servisidir.

## 🚀 Proje Özellikleri

* **Full-Stack Mimari:** Python (Flask) backend ve HTML/CSS/JS frontend entegrasyonu.
* **Flask API:** Ödeme ve indirim hesaplamaları için RESTful endpointler.
* **Modern Web Arayüzü:** Kullanıcı dostu, interaktif indirim hesaplama paneli.
* **Unit Testing:** `pytest` ile yüksek kod kapsamı (test coverage).
* **CI/CD Pipeline:** GitHub Actions ile her push işleminde otomatik test ve hata denetimi.
* **Logging & İzlenebilirlik:** Tüm işlemlerin `megamarket.log` dosyasına tarih/saat damgalı kaydı.
* **Validation:** Hatalı veri girişlerine karşı güçlü hata yakalama mekanizması.

## 🛠️ Kullanılan Teknolojiler

* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
* **Test/Analiz:** Pytest, Pytest-cov, Flake8
* **Otomasyon:** GitHub Actions

## 💻 Kurulum ve Çalıştırma

1. Projeyi klonlayın: `git clone https://github.com/YukselR1/CI-CD-Pipeline.git`
2. Sanal ortamı oluşturun ve aktif edin: `python -m venv venv` -> `.\venv\Scripts\activate`
3. Bağımlılıkları yükleyin: `pip install -r requirements.txt`
4. Uygulamayı başlatın: `python -m app.main`
5. Tarayıcıdan erişin: `http://127.0.0.1:5000`
