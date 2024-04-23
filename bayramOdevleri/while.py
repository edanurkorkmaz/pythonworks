toplam = 0 
while True:  
    giris = input("Bir sayı girin veya çıkmak için 'q' tuşuna basın: ")

    if giris.lower() == 'q': 
        break
    try:
        sayi = float(giris) 
        toplam += sayi 
        
    except ValueError:
        print("Geçersiz giriş! Lütfen bir sayı girin.")
print("Toplam:", toplam)
