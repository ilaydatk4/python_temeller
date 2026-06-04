import logging

# 1. Adım: Loglama sistemini ayarlıyoruz. 
# Hataları "uygulama.log" dosyasına, saat-tarih ve önem derecesiyle yazmasını söylüyoruz.
logging.basicConfig(
    filename='uygulama.log',
    filemode='a', # 'a' (append) yani üzerine ekleyerek yaz demektir
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO # INFO ve üzerindeki tüm logları kaydet
)

print("🚀 [SİSTEM]: Loglama simülasyonu başlatıldı...")
logging.info("Uygulama başarıyla ayağa kalktı.")

try:
    print("📂 Bir dosya açılmaya çalışılıyor...")
    logging.info("Sistem 'olmayan_rapor.txt' dosyasını okumaya çalışıyor.")
    
    # Bilerek olmayan bir dosyayı açmaya çalışıp hata fırlatıyoruz
    with open("olmayan_rapor.txt", "r") as dosya:
        icerik = dosya.read()
        
except FileNotFoundError as e:
    # Hata ekrana basılmıyor, arkadaki log dosyasına sessizce işleniyor!
    logging.error(f"Kritik Hata! İstenen dosya bulunamadı. Detay: {e}")
    print("⚠️ [SİSTEM]: Bir hata oluştu ama arkadaki günlük defterine (log) kaydedildi.")

logging.info("Uygulama güvenli bir şekilde kapatıldı.")
print("✅ [SİSTEM]: İşlem tamam.")
