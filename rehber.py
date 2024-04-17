rehber = {}

def kisi_ekle():
    isim = input("Kişinin adını girin: ")
    telefon = input("Kişinin telefon numarasını girin: ")
    rehber[isim] = telefon
    print(f"{isim} rehbere eklendi.")

def kisi_ara():
    isim = input("Aranacak kişinin adını girin: ")
    if isim in rehber:
        print(f"{isim}: {rehber[isim]}")
    else:
        print(f"{isim} rehberde bulunamadı.")

def rehberi_goster():
    if rehber:
        print("Rehberinizdeki kişiler:")
        for isim, telefon in rehber.items():
            print(f"{isim}: {telefon}")
    else:
        print("Rehberiniz şu anda boş.")

while True:
    print("\nYapabileceğiniz işlemler:")
    print("1. Kişi Ekle")
    print("2. Kişi Ara")
    print("3. Rehberi Göster")
    print("4. Çıkış")

    secim = input("Lütfen yapmak istediğiniz işlemi seçin: ")

    if secim == "1":
        kisi_ekle()
    elif secim == "2":
        kisi_ara()
    elif secim == "3":
        rehberi_goster()
    elif secim == "4":
        print("Rehber uygulamasından çıkılıyor.")
        break
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
