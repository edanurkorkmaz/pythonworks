title = "Python ile Programlama Dersleri"

# print(len(title)) karakter sayısı nedir?

# print(title[:6]) python kelimesini aldık.

# print(title[:5])
# print(title[-5:]) ilk 5 ve son 5 karakter.

# print(title[::-1])

ad = input("ad: ")
soyad = input("soyad: ")
not1 = input("not1: ")
not2 = input("not2: ")
ortalama = (float(not1)+ float(not2)) / 2

sonuc = f"{ad} {soyad} isimli öğrencinin 1.notu : {not1}, 2.notu : {not2} ve not ortalaması : {ortalama} dır."
print(sonuc)
