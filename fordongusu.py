#numbers = [1, 2, 3, 4, 5]

#for num in numbers:
 #   print(num)
 #----------------------------------------
#names = ["eda","sude","sıla"]
 
#for name in names:
 #    print(f"my name is {name}")
 #----------------------------------------
 
#name = "edanur korkmaz"

#for n in name:
  #  print(n)
#-----------------------------------------
sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# Sayilar listesindeki hangi sayılar 3' ün katıdır ?

#for num in sayilar:
 #   if(num % 3 == 0):
  #   print(num)
     
#--------------------------------------------------
# Sayilar listesinde sayıların toplamı kaçtır ?
#toplam = 0
#for sayi in sayilar:
 #   toplam += sayi
#print(f"toplam: ",toplam)
#--------------------------------------------------
#Sayilar listesindeki tek sayıların karesini alınız.
#for sayi in sayilar:
 #   if(sayi %2 == 1):
  #      print(sayi**2)
#--------------------------------------------------
#- Şehirlerden hangileri en fazla 5 karakterlidir ?

#sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

#for sehir in sehirler:
#    if(len(sehir)>5):
 #       print(sehir)
 #---------------------------------------------------
# Ürünlerin fiyatları toplamı nedir ?

urunler = [
  {'name':'samsung S6', 'price': '3000' },
  {'name':'samsung S7', 'price': '4000' },
  {'name':'samsung S8', 'price': '5000' },
  {'name':'samsung S9', 'price': '6000' },
  {'name':'samsung S10', 'price': '7000' }
]
#toplam = 0
#for urun in urunler:
 #  fiyat = int(urun["price"])
  # toplam += fiyat
#print(f"toplam ürün fiyatı:",toplam)
#-------------------------------------------------------
#Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

#for urun in urunler:
 #if(int(urun["price"]) <= 5000):
  #    print(urun["name"])