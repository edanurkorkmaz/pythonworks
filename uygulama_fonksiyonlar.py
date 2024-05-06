# Bankamatik Uygulaması

# Hesap bilgileri tutulacak(dict)
# menü, para çekme ,bakiye sorgula,param yatırma gibi fonksiyonlar tanımlanacak.
# çekilmek istenen tutar hesapta yok ise ek hesap tanımlanacak.

# hesaplar = [
#     {
#         "ad":"Sadık Turan",
#         "hesapNo":"12345",
#         "bakiye": 20000,
#         "ekHesap":5000,
#         "username":"sadikturan",
#         "password":"1234"
#     }, 
#     {
#         "ad":"Efe Turan",
#         "hesapNo":"12345",
#         "bakiye": 30000,
#         "ekHesap":10000,
#         "username":"efeturan",
#         "password":"1234"
#     }
# ]

# def menu(hesap):
#     print("\n")

#     print(f"merhaba, {hesap["ad"]}")

#     print("1- Bakiye sorgulama")
#     print("2- Para Çekme")
#     print("3- Para Yatırma")

#     islem = input("Yapmak istediğiniz işlem: ")

#     if islem == "1":
#         bakiyeSorgula(hesap)
#     elif islem == "2":
#         paraCekme(hesap)
#     elif islem == "3":
#         paraYatırma(hesap)
#     else:
#         print("Yanlış seçim")

#     menu(hesap)

# def paraYatırma(hesap):
#     pass
# def bakiyeSorgula(hesap):
#     print(f"bakiye: {hesap["bakiye"]}")
#     print(f"ek bakiye: {hesap["ekHesap"]}")

# def paraCekme(hesap):
#     miktar = float(input("çekmek istediğiniz miktar "))

#     if hesap["bakiye"] >= miktar:
#         hesap["bakiye"] -= miktar
#         print("paranızı alabilirsiniz.")
#     else:
#         toplam = hesap["bakiye"] + hesap["ekHesap"]

#         if toplam >= miktar:
#             ekHesapKullanimIzni = input("ek hesap kullanılsın mı? (e/h): ")

#             if ekHesapKullanimIzni == "e":
#                 kullanilacakMiktar = miktar-hesap["bakiye"]
#                 hesap["bakiye"] = 0
#                 hesap["ekHesap"] -= kullanilacakMiktar
#                 print("paranızı çekebilirsiniz.")

#             else:
#                 print("üzgünüz bakiyeniz yetersiz.")
#         else:
#          print("üzgünüz izin yok.")


# def login():
#     username = input("username: ")
#     password = input("parola: ")

#     isLoggedIn = False

#     for hesap in hesaplar:
#         if hesap["username"] == username and hesap["password"] == password:
#             isLoggedIn = True
#             menu(hesap)
#             break
#     if not(isLoggedIn):
#         print("username yada parola yanlış")
# login()        


# Bir Python fonksiyonu yazmanız gerekiyor. Bu fonksiyon, 
# verilen bir listenin içindeki sayıları alıp toplamını hesaplayacak ve 
# sonucu döndürecek. Fonksiyonun adı topla_liste olsun. Bir örnek olarak, 
# fonksiyona [1, 2, 3, 4, 5] listesi verildiğinde, döndürülen sonuç 15 olmalı.


# def topla_liste(liste):
#     toplam = 0
#     for sayi in liste:
#         toplam += sayi
#     return toplam

# liste = [1, 2, 3, 4, 5, 6]
# sonuc = topla_liste(liste)
# print("Toplam:", sonuc)



# Bir fonksiyon yazmanız gerekiyor. Bu fonksiyon, verilen bir string içindeki 
# her kelimenin baş harflerini alacak ve birleştirilmiş yeni bir string döndürecek.
# Fonksiyonun adı bas_harfler olsun. Örneğin, fonksiyona
# "Python programlama dili" girdi olarak verildiğinde, döndürülen sonuç "PPD" olmalı.

# def bas_harfler(cumle):
#     kelimeler = cumle.split()
#     sonuc = ""

#     for kelime in kelimeler:
#         sonuc += kelime[0]
#     return sonuc

# cumle = "Edanur Python Öğreniyor."
# sonuc = bas_harfler(cumle)
# print("Baş harfler:", sonuc)

# Bir fonksiyon yazmanız gerekiyor. Bu fonksiyon, verilen bir tam sayı 
# listesindeki çift sayıları ayıklayıp geri döndürecek. Fonksiyonun adı
# cift_sayilari_ayikla olsun. Bir örnek olarak, fonksiyona [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# listesi verildiğinde, döndürülen sonuç [2, 4, 6, 8, 10] olmalı

def cift_sayilari_ayikla(liste):
    cift_sayilar = []
    for sayi in liste:
        if sayi % 2 == 0:
            cift_sayilar.append(sayi)
    return cift_sayilar

sayi_listesi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_sonuclar = cift_sayilari_ayikla(sayi_listesi)
print("Çift sayılar:", cift_sonuclar)












 



