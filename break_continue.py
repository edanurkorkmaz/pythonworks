# isim = "edanur korkmaz"

# for harf in isim:
#     if (harf == "k"):
#        continue
#     print(harf)

# i = 0

# while(i < 5):
#     i += 1
#     if(i==2):
#         continue
#     print(i)
  

# for i in range(1,100,5):
#     print(i)

# 1'den 20'ye kadar sayılar içeren bir liste oluşturun.
# Bu listedeki her elemanın karesiyle yeni bir liste oluşturun.

# sayilar = list(range(1,5))

# karesi = [x ** 2 for x in sayilar] # list comprehenision

# print(sayilar)
# print(karesi)

# liste = list(range(1,31))

# ciftSayilar = [x for x in liste if x % 2 == 0]
# tekSayilar = [x for x in liste if x % 2 == 1]

# print(ciftSayilar)
# print(tekSayilar)

# liste = list(range(1,50))

# uce_bolunenler = [x for x in liste if x % 3 == 0]
# bese_bolunenler = [x for x in liste if x % 5 == 0]
# ortak = [x for x in liste if x % 3 == 0 and x % 5 == 0]

# print(uce_bolunenler)
# print(bese_bolunenler)
# print(ortak)

# numara = [100,200,300]
# isimler = ["eda","ayşe","fatma"]

# print(list(zip(numara,isimler)))

# "Bir mağazada ürünlerin isimlerinin ve fiyatlarının bulunduğu bir liste var.
# enumerate fonksiyonunu kullanarak her ürünün indeksini 
# ve fiyatını yüzde 10 artırarak yeni bir liste oluşturmak için bir Python kodu yazınız."

ürünler = [
    ("tv", 10000),
    ("telefon", 5000),
    ("beyazeşya", 50000),
    ("koltuk", 30000),
]

zamlı_ürünler = []

for indeks, (ürün, fiyat) in enumerate(ürünler):
    yeni_fiyat = fiyat * 1.10 
    zamlı_ürünler.append((indeks, ürün, yeni_fiyat))  

for indeks, ürün, fiyat in zamlı_ürünler:
    print(f"Ürün İndeksi: {indeks}, Ürün Adı: {ürün}, Zamlı Fiyat: {fiyat:.2f}")  
