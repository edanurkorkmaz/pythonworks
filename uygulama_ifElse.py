# yazili1 = float(input("yazili1: "))
# yazili2 = float(input("yazili2: "))
# sözlü = float(input("sözlü:"))

# ortalama = (yazili1 + yazili2 + sözlü) / 3
# print(ortalama)

# if (ortalama>0 and ortalama < 25):
#     print("notunuz 0")
# elif(ortalama>=25 and ortalama < 45):
#     print("notunuz 1")
# elif(ortalama>=45 and ortalama < 55):
#     print("notunuz 2")
# elif(ortalama>=55 and ortalama < 70):
#     print("notunuz 3")
# elif(ortalama>=70 and ortalama < 84):
#     print("notunuz 4")
# elif(ortalama>=85 and ortalama <= 100):
#     print("notunuz 5")
# else:
#     print("yanlış not bilgisi")

# benzinFiyat = 39.35
# dizelFiyat = 41.71
# lpgFiyat = 20.28

# toplamYakitUcreti = 0
# yakitTürü = input("yakıt türünü giriniz:")
# yol = float(input("gidilecek yol kaç km: "))
# ortalamaYakit =float(input("aracınız 100 km de ortalama ne kadar yakiyor: "))

# toplamYakitTüketimi = yol * (ortalamaYakit / 100)

# if(yakitTürü == "benzin"):
#     toplamYakitUcreti = benzinFiyat * toplamYakitTüketimi
# elif(yakitTürü == "lpg"):
#     toplamYakitUcreti = lpgFiyat * toplamYakitTüketimi
# elif(yakitTürü == "dizel"):
#     toplamYakitUcreti = dizelFiyat * toplamYakitTüketimi
# else:
#     print("Yanlış yakit tipi")

# if(toplamYakitUcreti != 0):
#     print(toplamYakitUcreti)


# Bir mağazada indirim oranları müşteri tipine göre değişmektedir. Mağaza, müşterilerini "Öğrenci", "Asker", 
# "Emekli" veya "Diğer" kategorilerine ayırır ve her bir kategori için farklı indirim oranları uygular:

# "Öğrenci" müşteriler için %20 indirim
# "Asker" müşteriler için %15 indirim
# "Emekli" müşteriler için %10 indirim
# "Diğer" müşteriler için herhangi bir indirim y

# musteriTipi = input("Müşteri Tipini Giriniz: ")
# toplamFiyat = int(input("Toplam Fiyat Giriniz: "))

# indirimOrani = 0  

# if musteriTipi == "öğrenci":
#     indirimOrani = 20
# elif musteriTipi == "asker":
#     indirimOrani = 15
# elif musteriTipi == "emekli":
#     indirimOrani = 10
# else:
#     print("Yanlış tipleme")
#     indirimOrani = 0  

# if indirimOrani > 0:
#     indirimMiktari = (toplamFiyat * indirimOrani) / 100
#     toplamFiyat = toplamFiyat - indirimMiktari

# print("İndirim Oranı:", indirimOrani)
# print("İndirimli Fiyat:", toplamFiyat)

# Kullanıcıdan iki sayı ve bir işlem türü (toplama, çıkarma, çarpma, bölme) alın. 
# Ardından, bu iki sayı ile belirtilen işlemi yapan ve sonucu yazdıran bir Python programı yazınız.

# sayi1 = float(input("1.sayıyı giriniz: "))
# sayi2 = float(input("2.sayıyı giriniz: "))
# islemTürü = input("İşlem Türü Seçiniz: ")
# sonuc = None

# if(islemTürü == "toplama"):
#     sonuc = sayi1 + sayi2
# elif(islemTürü == "çıkarma"):
#     sonuc = sayi1 - sayi2
# elif(islemTürü == "çarpma"):
#     sonuc = sayi1 * sayi2
# elif(islemTürü == "bölme"):
#     if sayi2 == 0:
#         print("Hata: Sıfıra bölme yapılamaz.")
#         sonuc = None
#     else:
#         sonuc = sayi1 / sayi2
# else:
#     print("geçersiz işlem girdiniz.")

# print(sonuc)

# Bir hava durumu uygulaması için bir liste düşün. Bu listede, 7 günlük hava durumu tahminleri 
# var. Her eleman, o günkü sıcaklığı temsil ediyor. Kullanıcıdan sıcaklık eşiği (threshold) 
# olarak bir sayı girmesini iste. Ardından, bu eşiğe göre sıcak ya da soğuk günleri ayır. 
# Eğer sıcaklık, kullanıcıdan alınan eşikten büyükse "sıcak",
# eşit ya da küçükse "soğuk" olarak düşün.

# sicakliklar = [23,15,8,30,12,7,22,36,19,28]

# derece = int(input("derece giriniz:"))

# hotdays = []
# colddays = []

# for temp in sicakliklar:
#     if temp > derece:
#         hotdays.append(temp)
#     else:
#         colddays.append(temp)

# print("sıcak günler: ", hotdays)
# print("soğuk günler:", colddays)

