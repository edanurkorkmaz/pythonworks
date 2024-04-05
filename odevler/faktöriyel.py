factorial = 1
sayi = int(input("Bir sayı girin: "))

if sayi >= 0:
     for i in range(1, sayi + 1):
        factorial *= i
     print(f"Girdiğiniz sayının faktöriyeli: {sayi}! = {factorial}")
try:
    if sayi < 0:
        raise ValueError("Negatif bir sayı giremezsiniz.")
except ValueError as hata:
    print(hata)
