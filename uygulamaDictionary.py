# satis_verileri = {
#     'Kitap A': 10,
#     'Kitap B': 5,
#     'Kitap C': 7
# }

# fiyat_verileri = {
#     'Kitap A': 20,
#     'Kitap B': 15,
#     'Kitap C': 25
# }

# kitapA = satis_verileri['Kitap A'] * fiyat_verileri['Kitap A']
# kitapB = satis_verileri['Kitap B'] * fiyat_verileri['Kitap B']
# kitapC = satis_verileri['Kitap C'] * fiyat_verileri['Kitap C']
# toplamGelir = kitapA + kitapB + kitapC
# print(toplamGelir)

# urunler = {
#     "bilgisayar":"1500",
#     "telefon":"800",
#     "tablet":"300",
#     "kulaklık":"50"
# }
# urun_sayisi = urunler.keys()
# urun = urun_sayisi
# print(len(urunler))

# sonuc = urunler.get("tablet")
# print(sonuc)

# urunler.update({"airpods":"250"})
# print(urunler)

# urunler.pop("tablet")
# print(urunler)

# isimler = list(urunler.keys())

# print(isimler)

not_defteri = {
    "Ali": [75, 82, 88],
    "Ayşe": [90, 85, 92],
    "Mehmet": [68, 74, 80],
    "Fatma": [95, 88, 91]
}

notAli = (not_defteri["Ali"][0] + not_defteri["Ali"][1] + not_defteri["Ali"][2]) / 3
notAyşe = (not_defteri["Ayşe"][0] + not_defteri["Ayşe"][1] + not_defteri["Ayşe"][2]) / 3
notMehmet = (not_defteri["Mehmet"][0] + not_defteri["Mehmet"][1] + not_defteri["Mehmet"][2]) / 3
notFatma = (not_defteri["Fatma"][0] + not_defteri["Fatma"][1] + not_defteri["Fatma"][2]) / 3

# print(notAli)
# print(notAyşe)
# print(notMehmet)
# print(notFatma)

# notu = not_defteri.get("Mehmet")
# print(notu)

# hepsi = not_defteri.items()
# print(hepsi)

# not_defteri.update({"eda":[45,65,98]})
# print(not_defteri)

# not_defteri.pop("eda")
# print(not_defteri)

# varmi = "Mehmet" in not_defteri
# print(varmi)