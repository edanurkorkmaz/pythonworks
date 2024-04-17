def kontrol_sayi(sayi):
    if sayi % 2 == 0:
        return sayi
    else:
        raise ValueError(f"{sayi} tek sayıdır.")

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sayi in liste:
    try:
        sonuc = kontrol_sayi(sayi)
        print(f"{sonuc} çift sayıdır.")
    except ValueError as e:
        print(e)