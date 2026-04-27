// Sayfa yüklendiğinde geçmişi getir
document.addEventListener('DOMContentLoaded', gecmisiYukle);

async function hesapla() {
    const total = document.getElementById('total').value;
    const discount = document.getElementById('discount').value;
    const resultBox = document.getElementById('result-box');
    const finalPriceText = document.getElementById('final-price');

    // Boş giriş kontrolü
    if (!total || !discount) {
        alert("Lütfen tüm alanları doldurun!");
        return;
    }

    const response = await fetch('/indirim', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            toplam_tutar: parseFloat(total),
            indirim_orani: parseFloat(discount)
        })
    });

    const data = await response.json();

    if (data.durum === "basarili") {
        finalPriceText.innerText = data.yeni_tutar;
        resultBox.classList.remove('hidden');
        // Hesaplama başarılıysa tabloyu hemen güncelle
        gecmisiYukle(); 
    } else {
        alert("Hata: " + data.hata);
    }
}

async function gecmisiYukle() {
    try {
        const response = await fetch('/gecmis');
        const islemler = await response.json();
        const tbody = document.getElementById('history-body');
        
        tbody.innerHTML = ''; // Tabloyu temizle

        islemler.forEach(islem => {
            // Backend'den gelen string tarihi JavaScript Date nesnesine çeviriyoruz
            // Eğer backend'den formatlı geliyorsa direkt basabilirsin, 
            // ama bu yöntem tarayıcı saatine göre en garanti yoldur.
            const tarihObj = new Date(islem.tarih);
            const formatliTarih = new Intl.DateTimeFormat('tr-TR', {
                day: '2-digit',
                month: '2-digit',
                year: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
            }).format(tarihObj);

            const row = `
                <tr style="border-bottom: 1px solid #eee; height: 45px; text-align: center;">
                    <td>${formatliTarih}</td>
                    <td>${islem.tutar} TL</td>
                    <td>%${islem.oran}</td>
                    <td style="color: #27ae60;"><strong>${islem.sonuc} TL</strong></td>
                </tr>
            `;
            tbody.innerHTML += row;
        });
    } catch (error) {
        console.error("Geçmiş yüklenirken hata oluştu:", error);
    }
}