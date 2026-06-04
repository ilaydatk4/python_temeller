# Kullanıcıdan iki sayı aldığımızı varsayalım
sayi1 = 10
sayi2 = 0  # Matematikte sıfıra bölünme hatası (ZeroDivisionError) tetikleyecek!

print("🛡️ [SİSTEM]: Zırh devreye giriyor...")

try:
    # Python'a diyoruz ki: "Şu işlemi yapmayı DENE (try)"
    sonuc = sayi1 / sayi2
    print(f"Sonuç: {sonuc}")

except ZeroDivisionError:
    # "Eğer yukarıdaki kod Sıfıra Bölünme Hatası verirse buraya zıpla (except)"
    print("⚠️ [HATA YAKALANDI]: Bir sayı sıfıra bölünemez cane! Programı çökertmek yerine güvenli limana aldım.")

except Exception as e:
    # "Eğer akla gelmedik BAŞKA bir hata olursa onu da burada yakala"
    print(f"🧐 [FARKLI HATA]: Beklenmeyen bir durum oluştu: {e}")

print("🚀 [SİSTEM]: Gördüğün gibi program çökmedi, hayat devam ediyor ve bu satır çalıştı!")
