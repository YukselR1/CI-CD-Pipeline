# tests/test_payment.py
import pytest
from app.payment import indirim_hesapla, odeme_yap

# --- İNDİRİM TESTLERİ ---

def test_normal_indirim_hesapla():
    # 100 TL'ye %20 indirim -> 80 TL kalmalı
    assert indirim_hesapla(100, 20) == 80

def test_hatali_indirim_orani():
    # %150 indirim olamaz, ValueError bekliyoruz
    with pytest.raises(ValueError):
        indirim_hesapla(100, 150)

# --- ÖDEME TESTLERİ ---

def test_normal_odeme_yap():
    # 500 TL bakiye, 200 TL harcama -> 300 TL kalmalı
    assert odeme_yap(500, 200) == 300

def test_yetersiz_bakiye():
    # 100 TL bakiye ile 200 TL ödenemez
    with pytest.raises(ValueError):
        odeme_yap(100, 200)

def test_negatif_odeme():
    # -50 TL gibi bir ödeme tutarı olamaz
    with pytest.raises(ValueError):
        odeme_yap(500, -50)