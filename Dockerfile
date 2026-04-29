# 1. Hafif bir Python imajı kullanıyoruz
FROM python:3.9-slim

# 2. Çalışma dizinini ayarlıyoruz
WORKDIR /app

# 3. Bağımlılıkları kopyalayıp yüklüyoruz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Tüm proje dosyalarını içeri kopyalıyoruz
COPY . .

# 5. Flask'ın dış dünyadan erişilebilir olması için portu açıyoruz
EXPOSE 5000

# 6. Uygulamayı başlatıyoruz
CMD ["python", "-m", "app.main"]