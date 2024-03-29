
kisiler = []

def kisi_ekle(ad, soyad):
    kisi = {'ad': ad, 'soyad': soyad}
    kisiler.append(kisi)
    print(f"{ad} {soyad} kişisi eklendi.")

def kisi_sil(ad, soyad):
    for kisi in kisiler:
        if kisi['ad'] == ad and kisi['soyad'] == soyad:
            kisiler.remove(kisi)
            print(f"{ad} {soyad} kişisi silindi.")
            return
    print(f"{ad} {soyad} kişisi bulunamadı.")

def kisi_ara(ad, soyad):
    for kisi in kisiler:
        if kisi['ad'] == ad and kisi['soyad'] == soyad:
            print(f"{ad} {soyad} kişisi aranıyor...")
            return
    print(f"{ad} {soyad} kişisi bulunamadı.")


def kisi_say(ad):
    count = sum(1 for kisi in kisiler if kisi['ad'] == ad)
    print(f"{ad} kişisinin sayısı: {count}")


def kisileri_goster():
    if len(kisiler) == 0:
        print("Listede hiç kişi yok.")
        return
    print("Kişiler:")
    for kisi in kisiler:
        print(f"{kisi['ad']} {kisi['soyad']}")


while True:
    print("\n1. Kişi Ekle")
    print("2. Kişi Sil")
    print("3. Kişi Ara")
    print("4. Kişi Say")
    print("5. Kişileri Göster")
   

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == '1':
        ad = input("Kişinin adını girin: ")
        soyad = input("Kişinin soyadını girin: ")
        kisi_ekle(ad, soyad)
    elif secim == '2':
        ad = input("Silmek istediğiniz kişinin adını girin: ")
        soyad = input("Silmek istediğiniz kişinin soyadını girin: ")
        kisi_sil(ad, soyad)
    elif secim == '3':
        ad = input("Aramak istediğiniz kişinin adını girin: ")
        soyad = input("Aramak istediğiniz kişinin soyadını girin: ")
        kisi_ara(ad, soyad)
    elif secim == '4':
        ad = input("Sayısını öğrenmek istediğiniz kişinin adını girin: ")
        kisi_say(ad)
    elif secim == '5':
        kisileri_goster()
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")