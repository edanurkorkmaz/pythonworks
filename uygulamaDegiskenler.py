name = "Edanur Korkmaz"
number = "05321234567"
email = "korkmaze101@gmail.com"
city = "Sivas"

urunAdi1 = "Kablosuz Mouse"
fiyat1 = 550

urunAdi2 = "Kablosuz Klavye"
fiyat2 = 650

urunAdi3 = "Dizüstü Bilgisyar"
fiyat3 = 55.000

urunToplami = (fiyat1 + fiyat2 + fiyat3)
kdvMiktar =(urunToplami * (18/100))
toplamAlinan = urunToplami + kdvMiktar

print("Alınan Ürünlerin Toplamı:" + str(urunToplami))
print("KDV miktarı: " + str(kdvMiktar))
print("toplam ödenecek tutar : " + str(toplamAlinan))
# print(type(kdvMiktar))
# print(type(toplamAlinan))
# print(type(urunToplami))