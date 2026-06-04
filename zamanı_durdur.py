isimler = ["Ahmet", "Mehmet", "İlayda", "Canan"]

print("🔄 Döngü başlıyor, isimleri tek tek kontrol edeceğiz...")

for sira, isim in enumerate(isimler, 1):
    print(f"Sıradaki isim işleniyor: {isim}")
    
    if isim == "İlayda":
        print("🚨 [DİKKAT]: 'The Architect' bulundu! Kod donduruluyor...")
        # İşte o meşhur durdurma butonu! Kod tam burada donacak!
        breakpoint()
        
    print(f"✨ {isim} başarıyla işlendi.")

print("🏁 Döngü bitti, kod normal akışına döndü.")
