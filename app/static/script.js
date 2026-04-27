async function hesapla() {
    const total = document.getElementById('total').value;
    const discount = document.getElementById('discount').value;
    const resultBox = document.getElementById('result-box');
    const finalPriceText = document.getElementById('final-price');

    // Backend'e (Flask) istek atıyoruz
    const response = await fetch('/indirim', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            toplam_tutar: parseFloat(total),
            indirim_orani: parseFloat(discount)
        })
    });

    const data = await response.json();

    if (data.durum === "basarili") {
        finalPriceText.innerText = data.yeni_tutar;
        resultBox.classList.remove('hidden'); // Sonuç kutusunu göster
    } else {
        alert("Hata: " + data.hata);
    }
}