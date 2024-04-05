sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

def EKOK(a, b):
   
    max_sayi = max(a, b)
    for i in range(max_sayi, a * b + 1, max_sayi):
        if i % a == 0 and i % b == 0:
            return i

print("Verilen iki sayının Ekok'u:", EKOK(sayi1, sayi2))