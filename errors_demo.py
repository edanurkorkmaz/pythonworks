liste = ["1","2","5a","10b","abc","10","50"]

#1-liste elemanları içindeki sayısal değerleri bulunuz.
# for x in liste:
#     try:
#       sonuc = int(x)
#       print(sonuc)
#     except ValueError:
#      continue

#2-kullanıcı "q" değerini girmedikçe aldığınız 
# her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.

# while True:
#     sayi = input("sayı: ")
#     if(sayi == "q"):
#         break
#     try:
#         sonuc = float(sayi)
#         print(f"girilen sayı : {sayi}")
#         break
#     except ValueError:
#         print("geçersiz sayı")
#         continue

#3-girilen parola içinde türkçe karakter hatası veriniz.

def parolaKontrol(parola):
    turkce_karakterler = "şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("parola türkçe karakter içeremez.")
    print("geçerli parola")

parola = input("parola: ")

try:
    parolaKontrol(parola)
except TypeError as e:
    print(e)









# 4-faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.

# def faktoriyel(x):
#     x = int(x)

#     if x < 0 :
#         raise ValueError("negatif değer")
    
#     result = 1

#     for i in range(1, x+1):
#         result *= i
#     return result

# for i in [3,6,7,'2a',-1,-7,9]:
#     try:
#         x = faktoriyel(i)
#     except ValueError as e:
#         print(e)
#         continue
#     else:
#         print(x)




 