while True:
    print("\n--- Gider Takip Sistemi ---")
    print("1. Yeni Harcama Ekle")
    print("2. Harcamaları Listele")
    print("3. Toplam Tutarı Gör")
    print("4. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")

    if secim == "1":
        harcama_adi = input("Harcama kalemini girin: ")
        miktar = input("Harcama miktarını girin: ")
        with open("giderler.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"{harcama_adi},{miktar}\n")
        print("✔ Kaydedildi!")

    elif secim == "2":
        print("\n--- Kayıtlı Harcamalarınız ---")
        try:
            with open("giderler.txt", "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    satir = satir.strip()
                    if not satir or "," not in satir:
                        continue
                    ad, mik = satir.split(",")
                    print(f"- {ad}: {mik} TL")
        except FileNotFoundError:
            print("Dosya bulunamadı.")

    elif secim == "3":
        toplam = 0
        print("\n--- Toplam Hesaplanıyor ---")
        try:
            with open("giderler.txt", "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    satir = satir.strip()
                    if not satir or "," not in satir:
                        continue

                    ad, mik = satir.split(",")

                    try:
                        toplam += int(mik)
                    except ValueError:
                        print(f"⚠️ Hata: '{ad}' için girilen '{mik}' bir sayı değil, toplama eklenemedi.")

            print(f"💰 Toplam Harcama: {toplam} TL")
        except FileNotFoundError:
            print("Hesaplanacak veri bulunamadı.")

    elif secim == "4":
        print("Uygulamadan çıkılıyor... Hoşça kalın!")
        break

    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")