import os

# 1. Adım: Yeni bir klasör adı belirleyelim
klasor_adi = "Staj_Raporlari"

# 2. Adım: Eğer bu klasör bilgisayarda yoksa otomatik oluşturalım
if not os.path.exists(klasor_adi):
    os.makedirs(klasor_adi)
    print(f"🚀 [SİSTEM]: '{klasor_adi}' klasörü başarıyla oluşturuldu!")
else:
    print(f"⚠️ [SİSTEM]: '{klasor_adi}' klasörü zaten var, es geçiliyor.")

# 3. Adım: Oluşturduğumuz klasörün içine bir dosya yolu tanımlayalım
dosya_yolu = os.path.join(klasor_adi, "gunluk_rapor.txt")

# 4. Adım: Dosyayı açıp içine otomatik log yazalım
with open(dosya_yolu, "w", encoding="utf-8") as dosya:
    dosya.write("Mimar İlayda tarafından yazılan otomatik otomasyon raporudur.\n")
    print(f"📝 [SİSTEM]: Klasörün içine '{dosya_yolu}' başarıyla yazıldı!")
