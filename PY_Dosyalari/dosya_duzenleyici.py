import os
import shutil

# 1. Adım: Temizlenecek ve düzenlenecek hedef klasörü seçelim
# Test etmek için az önce açtığımız klasörü ve bir üst dizini hedef alabiliriz
hedef_klasor = "." # Nokta, şu an bulunduğumuz klasör demektir

# 2. Adım: Klasörün içindeki her şeyi tarayalım
print("🧹 [TEMİZLİK]: Düzenleme işlemi başlatılıyor...")

for dosya in os.listdir(hedef_klasor):
    # Klasörleri es geçelim, sadece dosyalarla ilgileniyoruz
    if os.path.isfile(dosya):
        # Dosyanın uzantısını bulalım (örn: .py, .txt, .env)
        dosya_adi, uzanti = os.path.splitext(dosya)
        uzanti = uzanti.lower().replace(".", "") # Noktayı atıp sadece 'py' veya 'txt' bırakıyoruz
        
        # Eğer gizli veya uzantısız bir dosyaysa es geç
        if not uzanti:
            continue
            
        # Uzantıya göre yeni bir klasör adı belirleyelim (örn: Python_Dosyalari)
        yeni_klasor_adi = f"{uzanti.upper()}_Dosyalari"
        
        # Klasör yoksa otomatik yarat
        if not os.path.exists(yeni_klasor_adi):
            os.makedirs(yeni_klasor_adi)
            
        # Dosyayı yeni klasörün içine taşıyalım (shutil.move gücü)
        shutil.move(dosya, os.path.join(yeni_klasor_adi, dosya))
        print(f"📦 [TAŞINDI]: {dosya} -> {yeni_klasor_adi} klasörüne postalandı!")

print("✅ [BAŞARI]: Klasör bir mimar titizliğiyle tertemiz yapıldı!")
