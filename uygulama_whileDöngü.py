# i = 1

# while i <= 5:
#     print(i)
#     i += 1

# i = 1
# sayilar = [1,2,3,4,5,6,7,8,9]

# while (i < len(sayilar)):
#     print(i)
#     i += 1

# baslangic = int(input("başlangıç:"))
# bitis = int(input("bitiş: "))

# i = baslangic
# while(i < bitis):
#     if (i % 2 == 0):
#       print(i)
#       i += 2
    
# sayilar = 100
# while (sayilar > 0):
#  print(sayilar)
#  sayilar -= 1


# i = 0
# sayilar = []

# while(i < 5):
#     sayi = int(input("sayı: "))
#     sayilar.append(sayi)
#     i += 1

# sayilar.sort()
# print(sayilar)

# username = ""

# while not username:
#     username = input("kullanıcı adı: ")
# print("girilen username: " + username )

# devammi = "e"
# ogrenciler = []

# while(devammi != "h"):
#     ogrenciNo = input("öğrenci no:")
#     ogrenciAd = input("öğrenci adı:")
#     ogrenciSoyad = input("öğrenci soyadı:")

#     ogrenciler.append({
#         "ogrenciNo": ogrenciNo,
#         "ogrenciAd": ogrenciAd,
#         "ogrenciSoyad": ogrenciSoyad,
#     })

#     devammi = input("devammı (e/h): ")

# for ogrenci in ogrenciler:
#     print(f"{ogrenci["ogrenciNo"]} numaralı öğrencinin adı {ogrenci["ogrenciAd"]}{ogrenci["ogrenciSoyad"]}")
              
# Bir tam sayı olan x belirlenmiş olsun. 
# Bu tam sayı ile bir toplama işlemi gerçekleştir. 
# Bir başlangıç değeri olan y = 0 ile başla ve her döngü adımında x kadar artırarak y'yi ekrana yazdır. 
# Döngü, y değeri 50'ye eşit veya daha büyük olduğunda sona ersin.

# y = 0
# x = 3

# while(y < 50):
#     print(y)
#     y += x

# Bir tam sayı değişkeni olan n belirlenmiş olsun.
# n'in faktöriyelini hesaplamak için bir döngü kullan. Faktöriyel, 1'den n'e kadar olan tüm sayıları çarpmanın sonucudur.
# Örnek olarak, n = 5 için faktöriyel, 5 x 4 x 3 x 2 x 1 = 120'dir.
# Bu faktöriyel hesaplama işlemini yapan bir kod yazabilir misin?

# n = int(input("n değeri giriniz:"))
# sonuc = 1  
# sayac = 1  

# while sayac <= n:
#     sonuc *= sayac 
#     sayac += 1  

# print(f"Faktöriyel({n}) = {sonuc}") 

# Bir kullanıcıdan girdi alarak, pozitif bir tam sayı olup olmadığını kontrol eden 
# ve negatif bir sayı girildiğinde kullanıcıdan tekrar pozitif bir sayı girmesini 
# isteyen bir kod yaz. Eğer girilen sayı pozitifse, 
# program "Pozitif sayı girdiğiniz için teşekkürler!" mesajını yazdırır ve döngüyü sonlandırır
# Bu senaryoyu kodlamak için bir 
# döngü kullan. Negatif veya sıfır bir sayı girildiğinde döngü devam eder 
# ve pozitif bir sayı girilene kadar kullanıcıdan girdi almaya devam eder.

# number = 0

# while number <= 0:
#     number = int(input("lütfen pozitif bir tam sayı giriniz: "))
#     if number <= 0:
#         print("pozitif tam sayı giriniz:")
# print("teşekkürler pozitif tam sayı girdiniz.")

# Bir liste (list) içindeki sayıların toplamını hesaplayan bir kod yazmanı istiyorum. 
# while döngüsü kullanarak listenin elemanlarını sırayla inceleyip toplamayı 
# gerçekleştirmelisin.
#  Kodun sonunda, bu toplamı ekrana yazdırmalısın.


# numbers = [1,2,3,4,5,6,7,8,9]  
# total = 0  
# index = 0  

# while index < len(numbers):
#     total += numbers[index]
#     index += 1 

# print(f"Liste içindeki toplam sayı sayısı:", len(numbers))
# print("Liste içindeki sayıların toplamı:", total) 

