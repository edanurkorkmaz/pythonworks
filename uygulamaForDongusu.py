# sayilar = [1,2,3,4,5,6,7,8,9]
# isimler = ["ahmet","ali","zeynep"]
# ad = "edanur korkmaz"
# for i in sayilar:
#     print(i)

# for i in isimler:
#     print(i)

# for i in ad:
#     print(i)

# my_tuple = [(1,2),(3,4),(5,6)]

# for a,b in my_tuple:
#     print(a,b)

# my_dict = {"41":"kocaeli","53":"rize","35":"izmir"}

# for x in my_dict:
#     print(my_dict[x])

# for x,y in my_dict.items():
#     print(x,y)

# sayilar = [3,5,7,2,12,32,45]

# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
# print(toplam)

# urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# for urun in urunler:

#     index = urun.find('iphone')
#     if index > -1:
#         print(urun)

# adet = 0 
# for urun in urunler:
#     index = urun.find("samsung")
#     if index > -1:
#         adet += 1
# print(adet)

# sayi_listesi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# toplam = 0 
# for sayi in sayi_listesi:
#     if sayi % 2 != 0:  
#         toplam += sayi
# print(toplam)


# metin = "Python programlama dilini öğrenmek eğlencelidir."
# aranan_harf = "e"

# harf_sayisi = 0
# for karakter in metin:
#     if karakter.lower() == aranan_harf.lower():  
#         harf_sayisi += 1  
# print(f"'{aranan_harf}' harfi metinde {harf_sayisi} kez geçiyor.")

# urunler = [
#     {"urunAdi":"Hp Victus","fiyat":"32999"},
#     {"urunAdi":"Lenovo ThinkPad","fiyat":"25499"},
#     {"urunAdi":"Apple Macbook","fiyat":"49999"},
#     {"urunAdi":"Huawei Matebook","fiyat":"26999"},
#     {"urunAdi":"Casper Nirvana","fiyat":"20000"}
# ]

# for urun in urunler:
#     print(f"{urun['urunAdi']} marka ürünün fiyatı {urun["fiyat"]} Türk lirasıdır.")

# toplam = 0
# for urun in urunler:
#     toplam += int(urun["fiyat"])
# print(f"toplam fiyat: {toplam}")

# for urun in urunler:
#     if int(urun["fiyat"]) > 25000 and int(urun["fiyat"]) < 40000:
#         print(urun["urunAdi"])

# kelime = input("Aramak istediğiniz ürün nedir? ")

# for urun in urunler:
#     if (urun["urunAdi"].lower().find(kelime.lower()) > -1):
#         print(f"{urun['urunAdi']}")

# Bir lisede bir sınıfta bulunan öğrencilerin sınav sonuçları var. 
# Sınıfta toplamda 30 öğrenci var. Her öğrencinin sınavdan aldığı puanları temsil eden bir liste verildi. 
# Puanlar 0 ile 100 arasında değişiyor.
# For döngüsünü kullanarak, öğrencilerin kaçının geçer not aldığını hesapla. 
# Geçer not, 50 veya üzeri olarak kabul ediliyor.
# Bunu başarmak için gereken adımlar şunlar:
# Öğrenci puanlarını temsil eden bir liste oluştur.
# For döngüsü ile tüm puanları kontrol et.
# Geçer not almış öğrencilerin sayısını hesapla.

# puanlar = [
#     {"ad":"eda","puan":"50"},
#     {"ad":"sude","puan":"60"},
#     {"ad":"sıla","puan":"45"},
#     {"ad":"cansu","puan":"85"},
#     {"ad":"elif","puan":"71"}
# ]

# puanlar.append({"ad":"ayşe","puan":"78"})

# for puan in puanlar:
#     if (int(puan["puan"]) > 50):
#         print(f" başarılı öğrenciler: {puan['ad']}")



        

