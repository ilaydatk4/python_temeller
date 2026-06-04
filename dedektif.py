def hesapla():
    # Olmayan bir değişkeni çağıralım (NameError tetikleyeceğiz)
    print(olmayan_degisken)

def ana_fonksiyon():
    print("🤖 İşlem başlatılıyor...")
    hesapla()

# Kodu tetikliyoruz
ana_fonksiyon()
