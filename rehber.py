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

<<<<<<< HEAD
# Kişi arama fonksiyonu
def kisi_ara(bilgi):
    for kisi in kisiler:
        if kisi['ad'] == bilgi or kisi['soyad'] == bilgi:
            print(f"{kisi['ad'], kisi['soyad']} kişisi aranıyor.")
            return
    print(f"{bilgi} kişisi bulunamadı.")
=======
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
>>>>>>> c391ffc18917467bb95b7afca50a2a01c7724156

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

<<<<<<< HEAD
    if secim == '1':
        ad = input("Kişinin adını girin: ")
        soyad = input("Kişinin soyadını girin: ")
        kisi_ekle(ad, soyad)
    elif secim == '2':
        ad = input("Silmek istediğiniz kişinin adını girin: ")
        soyad = input("Silmek istediğiniz kişinin soyadını girin: ")
        kisi_sil(ad, soyad)
    elif secim == '3':
       #ad = input("Aramak istediğiniz kişinin adını girin: ")
        #soyad = input("Aramak istediğiniz kişinin soyadını girin: ")
        bilgi=input("lütfen istediğiniz kişinin adını,soyadını veya numarasını girin: ")
        kisi_ara(bilgi)
    elif secim == '4':
        ad = input("Sayısını öğrenmek istediğiniz kişinin adını girin: ")
        soyad = input("Sayısını öğrenmek istediğiniz kişinin soyadını girin: ")
        kisi_say(ad, soyad)
    elif secim == '5':
        kisileri_goster()
    elif secim == '6':
        print("Programdan çıkılıyor...")
=======
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
>>>>>>> c391ffc18917467bb95b7afca50a2a01c7724156
        break
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
