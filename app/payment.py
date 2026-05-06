# app/payment.py

def indirim_hesapla(toplam_tutar, indirim_orani):
    """
    İndirim tutarını hesaplar. 
    Kural 1: İndirim oranı 0 ile 100 arasında olmalıdır.
    Kural 2: Toplam tutar negatif olamaz.
    """
    if indirim_orani < 0 or indirim_orani > 100:
        raise ValueError("İndirim oranı 0-100 arasında olmalıdır.")
    
    if toplam_tutar < 0:
        raise ValueError("Toplam tutar negatif olamaz.")
    
    indirim_miktari = (toplam_tutar * indirim_orani) / 100
    return toplam_tutar - indirim_miktari

def odeme_yap(bakiye, odenecek_tutar):
    """
    Ödeme işlemini gerçekleştirir.
    Kural 1: Ödenecek tutar bakiyeden büyük olamaz.
    Kural 2: Ödenecek tutar 0'dan büyük olmalıdır.
    """
    if odenecek_tutar <= 0:
        raise ValueError("Ödenecek tutar sıfırdan büyük olmalıdır.")
    
    if odenecek_tutar > bakiye:
        raise ValueError("Yetersiz bakiye!")
    
    yeni_bakiye = bakiye - odenecek_tutar
    return yeni_bakiye