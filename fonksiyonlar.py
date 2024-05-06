#def sayHello(name = "user"):
  #  return "hello "+ name

#msg = sayHello("çınar")
#msg = sayHello("ada")

#print(msg)

#def total(num1, num2):
 #   return num1 + num2

#result = total(10,20)
#result = total(15,20)

#print(result)


#def yasHesapla(dogumYili):
 #   return 2024 - dogumYili

#ageCınar = yasHesapla(2017)
#ageAda = yasHesapla(2010)
#ageSena = yasHesapla(1999)

#print(ageCınar, ageAda, ageSena)

# def EmekliligeKacYilKaldi(dogumYili,isim):
#     yas = 2024 - dogumYili
#     emeklilik= 65 - yas 
    
#     if emeklilik > 0:
#         print (f"emekliliğinize {emeklilik} yil kaldi.")
#     else:
#         print("zaten emekli oldunuz.")

# EmekliligeKacYilKaldi(2000, "ali")

# def selamlama():
#     for i in range(10):
#         print("selam")
# selamlama()

# def yil():
#     import datetime
#     return datetime.datetime.now().year

# def yasHesapla():
#     return yil() - 2000
# print(yasHesapla())

# def saat():
#     import datetime
#     return datetime.datetime.now().hour

# def selamlama():
#     if(saat() < 12):
#         return("günaydın")
#     else:
#         return("selam")
# print(selamlama())

# def selamlama(isim):
#     return "merhaba, " +isim
# print(selamlama("eda"))
# print(selamlama("ayça"))

# def yasHesapla(dogumYili):
#     return 2024 - dogumYili

# print(yasHesapla(2000))

# def emekliligeKacYilKaldi(dogumYili,isim):
#     yas = 2024 - dogumYili
#     emeklilik = 58 - yas

#     if emeklilik > 0:
#         print(f"{isim} kişisi emekliliğinize {emeklilik} yıl kaldı.")
#     else:
#         print(f"{isim} kişisi zaten emekli oldunuz.")

# emekliligeKacYilKaldi(2000, "eda")
# emekliligeKacYilKaldi(1960, "sıla")
# emekliligeKacYilKaldi(1993, "cansu")

#kendisine gönderilen bir kelimeyi belirtilen kez ekranda yazdırsın.
# def tekrar(text , adet):
#     return text * adet
# print(tekrar("merhaba ", 6))

# dikdörtgenin alanını ve çevresini hesaplayan fonksiyonu yazdırın.

# def hesapla (uzunkenar,kısakenar):
#     alan = uzunkenar * kısakenar 
#     çevre = (uzunkenar + kısakenar) * 2

#     return f"alan: {alan} çevre: {çevre}"
# sonuc = hesapla(10,10)
# print(sonuc)

# yazı tura uygulamasını fonksiyon kullanarak yapınız.

# def yaziTura():
#     import random
#     sayi = random.random()

#     if sayi > 0.5:
#         return "Tura"
#     else:
#         return "Yazı"

# print(yaziTura())

# kendisine gönderilen 2 sayı arasındaki asal sayıları yazdıran uygulamayı yapınız.

# def asalSayilariBul(sayi1 , sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if(sayi > 1):
#             for i in range(2,sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)
# asalSayilariBul(50,100)


# kendisine gönderilen bir sayının tam bölenlerini liste şeklinde yazdırınız.

# def tamBolenlerBul(sayi):
#     tamBolenler = []

#     for i in range(2,sayi):
#         if (sayi % i == 0):
#             tamBolenler.append(i)
#     return tamBolenler
# print(tamBolenlerBul(20)) 

# def selamlama(isim, mesaj = "iyi Günler"):
#     return f" {mesaj} {isim}"

# sonuc = selamlama("eda")
# sonuc = selamlama("eda","selam")

# def usAlma(taban,us = 2):
#     return taban ** us
# sonuc = usAlma(5,3)


# print(sonuc)

# def full_name(firstname, lastname):
#     return f"Your name is: {firstname} {lastname}"

# sonuc = full_name(lastname="korkmaz",firstname="eda")

# print(sonuc)



        
  















