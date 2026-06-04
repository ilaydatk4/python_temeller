# Fonksiyonumuzu tanımlarken parametrelerin yanına tiplerini yazıyoruz.
# 'fiyat: float' -> fiyatın ondalıklı sayı olacağını, 
# 'oran: int' -> indirim oranının tam sayı olacağını belirtir.
# '-> float' ise bu fonksiyonun geriye ondalıklı bir sayı döndüreceğini ilan eder (Type Hint).

def indirim_hesapla(fiyat: float, oran: int) -> float:
    """
    Bu fonksiyon kurumsal bir indirim hesaplama motorudur.
    """
    indirim_miktari = fiyat * (oran / 100)
    son_fiyat = fiyat - indirim_miktari
    return son_fiyat

# Şimdi bu mimariyi kullanalım
print("🏗️  [MİMARİ]: Fonksiyon tetikleniyor...")

urun_fiyati = 250.0
indirim = 20

# Fonksiyonu çağırıyoruz
odenecek_tutar = indirim_hesapla(urun_fiyati, indirim)

print(f"💰 Orijinal Fiyat: {urun_fiyati} TL")
print(f"📉 İndirim Oranı: %{indirim}")
print(f"✅ Ödenecek Son Tutar: {odenecek_tutar} TL")
