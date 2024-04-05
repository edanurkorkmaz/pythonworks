sayi = int(input("Sayı Giriniz: "))

toplam = 0

for i in range(1,sayi):
    if(sayi%i == 0):
        toplam += i
if(sayi == toplam):
    print("mükemmel sayıdır.")
else:
    print("mükemmel sayı değildir.")