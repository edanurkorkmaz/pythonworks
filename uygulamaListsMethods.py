# customers = ["sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
# order_totals = [12000,13000,5000,15000]

# customers.append("edanurkorkmaz")
# order_totals.append("5000")

# customers.pop()
# order_totals.pop()

# sonuc = f"{customers[0]} isimli müşterinin sipariş toplamı {order_totals[0]}liradır"
# sonuc1 = f"{customers[1]} isimli müşterinin sipariş toplamı {order_totals[1]}liradır"
# sonuc2 = f"{customers[2]} isimli müşterinin sipariş toplamı {order_totals[2]}liradır"
# sonuc3 = f"{customers[3]} isimli müşterinin sipariş toplamı {order_totals[3]}liradır"

# print(sonuc)
# print(sonuc1)
# print(sonuc2)
# print(sonuc3)

# customers.sort()
# order_totals.sort()
# order_totals.reverse()
# print(order_totals)
# print(customers)
# sonuc = min(order_totals)
# print(sonuc)
# print(customers)
# print(order_totals)

# sonuc = customers.count("sadikturan")
# print(sonuc)

# customers.remove("ahmetyilmaz")
# print(customers)

# customers.clear()
# order_totals.clear()

# username = input("ad: ")
# toplam = input("toplam: ")

# customers.append(username)
# order_totals.append(toplam)

# print(customers)
# print(order_totals)

# Liste Oluşturma ve Temel İşlemler
# 10 ile 50 arasında (dahil) çift sayıları içeren bir liste oluşturun.
# Boş bir liste oluşturup, sonra listeye "Python", "Java", "C++" gibi farklı programlama dilleri ekleyin.
# Bir listeyi tersine çevirmenin birden fazla yolunu yazın.


# cift_sayilar = list(range(1,50,2))
# print(cift_sayilar)

# list = []

# list.append("java")
# list.append("c++")
# list.append("python")

# print(list)

# numbers = [1,2,3,4,5,6,7,8,9]
# harf = ["a","b","k","t","h","y","c"]
# numbers.reverse()
# ücüncü_elemam = numbers[2]

# print(ücüncü_elemam)

# sonUcEleman = numbers[-3:]
# print(sonUcEleman)

# herIkinciEleman = numbers[::3]
# print(herIkinciEleman)

# numbers.insert(2,78)
# print(numbers)

# numbers.pop()
# numbers.remove(5)

# harf.sort()
# print(harf)

# tek_sayilar = [x for x in range(1,21) if x % 2 == 0]
# print(tek_sayilar)

# kareler_listesi = [x ** 2 for x in tek_sayilar]
# print(kareler_listesi)

# list = [1,2,3,3,5,4,6,3,3,4,6,3]
# ciftsayi = [x for x in list if x % 2 == 0]
# print(ciftsayi)

# toplam = sum(list)
# print(toplam)

# kackez = list.count(3)
# print(kackez)

# kelimeler = ["eda", "python", "öğreniyor."]
# birlestir = " ".join(kelimeler)
# print(birlestir)

