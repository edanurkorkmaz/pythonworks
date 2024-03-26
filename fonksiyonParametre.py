
#Gönderilen bir kelimeyi belirtilen kez ekranda gösteren python fonksiyonunu yazınız.

#def yazdir(kelime, adet):
 #   print(kelime * adet)
    
#yazdir("merhaba\n", 10)

# Kendisine gönderilen bir sayının tam bölenlerini bulan python uygulamasını yapınız.

#def listeyeCevir(*params):
 #   liste = []
    
  #  for param in params:
   #     liste.append(param)
        
    #    return liste
#result = listeyeCevir(10,20,30,"merhaba")
#print(result)

#Gönderilen 2 sayı arasındaki tüm asal sayıları bulan python fonksiyon uygulamasını yapınız.
#def asalSayılariBul(sayi1, sayi2):
 #   for sayi in range(sayi1, sayi2+1):
 #       if sayi > 1:
 #           for i in range(2, sayi):
 #               if (sayi % i == 0):
 #                   break
 #           else:
 #               print(sayi)

#sayi1 = int(input('sayı 1:'))
#sayi2 = int(input('sayı 2:'))

#asalSayılariBul(sayi1, sayi2)
# Kendisine gönderilen bir sayının tam bölenlerini bulan python uygulamasını yapınız.
#def tamBolenleriBul(sayi):
   # tamBolenler = []

   # for i in range(2, sayi):
    #    if (sayi % i == 0):
     #       tamBolenler.append(i)    

  #  return tamBolenler

# print(tamBolenleriBul(20))

def changeName(n):
   n = "ada"
name = "yiğit"
   
changeName(name) 
print(name)

def change(n):
   n[0] = "istanbul"
   
sehirler = ["ankara","izmir"]

change(sehirler)
print(sehirler)