rehber = {}

def kisi_ekle():
    isim = input("Kişinin adını girin: ")
    telefon = input("Kişinin telefon numarasını girin: ")
    rehber[isim] = telefon
    print(f"{isim} rehbere eklendi.")

def kisi_sil():
    isim = input("Silmek istediğiniz kişinin adını girin: ")
    if isim in rehber:
        del rehber[isim]
        print(f"{isim} rehberden silindi.")
    else:
        print(f"{isim} rehberde bulunamadı.")

def kisi_ara():
    arama = input("Arama yapmak istediğiniz ismi veya numarası girin: ")
    bulunanlar = []
    for isim, telefon in rehber.items():
        if arama.lower() in isim.lower() or arama in telefon:
            bulunanlar.append((isim, telefon))
    if bulunanlar:
        print("Arama Sonuçları:")
        for isim, telefon in bulunanlar:
            print(f"{isim}: {rehber[isim]} aranıyor..")
    else:
        print("Aranan kriterlere uygun kişi bulunamadı.")

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
    print("3. Kişi Sil")
    print("4. Rehberi Göster")
    print("5. Çıkış")

    secim = input("Lütfen yapmak istediğiniz işlemi seçin: ")

    if secim == "1":
        kisi_ekle()
    elif secim == "2":
        kisi_ara()
    elif secim == "3":
        kisi_sil()
    elif secim == "4":
        rehberi_goster()
    elif secim == "5":
        print("Rehber uygulamasından çıkılıyor.")
        break
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
