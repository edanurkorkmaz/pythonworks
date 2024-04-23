# Kişilerin tutulacağı bir liste oluşturalım
kisiler = []

# Kişi ekleme fonksiyonu
def kisi_ekle(ad, soyad):
    kisi = {'ad': ad, 'soyad': soyad}
    kisiler.append(kisi)
    print(f"{ad} {soyad} kişisi eklendi.")

# Kişi silme fonksiyonu
def kisi_sil(ad, soyad):
    for kisi in kisiler:
        if kisi['ad'] == ad and kisi['soyad'] == soyad:
            kisiler.remove(kisi)
            print(f"{ad} {soyad} kişisi silindi.")
            return
    print(f"{ad} {soyad} kişisi bulunamadı.")

# Kişi arama fonksiyonu
def kisi_ara(bilgi):
    for kisi in kisiler:
        if kisi['ad'] == bilgi or kisi['soyad'] == bilgi:
            print(f"{kisi['ad'], kisi['soyad']} kişisi aranıyor.")
            return
    print(f"{bilgi} kişisi bulunamadı.")

# Belirli bir koşulu sağlayan kişi sayısını bulma fonksiyonu
def kisi_say(ad, soyad):
    count = sum(1 for kisi in kisiler if kisi['ad'] == ad and kisi['soyad'] == soyad)
    print(f"{ad} {soyad} kişisinin sayısı: {count}")

# Tüm kişileri gösterme fonksiyonu
def kisileri_goster():
    if len(kisiler) == 0:
        print("Listede hiç kişi yok.")
        return
    print("Kişiler:")
    for kisi in kisiler:
        print(f"{kisi['ad']} {kisi['soyad']}")

# Ana döngü
while True:
    print("\n1. Kişi Ekle")
    print("2. Kişi Sil")
    print("3. Kişi Ara")
    print("4. Kişi Say")
    print("5. Kişileri Göster")
    print("6. Çıkış")

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
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")