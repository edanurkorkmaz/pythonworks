yemekTarifi = {
    "yemekAdi":"Musakka",
    "yemekTarifi":"tarif açıklaması",
    "resim":"1.jpg"
}

#access items
sonuc = yemekTarifi["yemekAdi"]
sonuc = yemekTarifi.get("yemekAdi") #musakka bilgisi yine gelir.
sonuc = yemekTarifi.keys()  # içerideki tüm key bilgilerini liste şeklinde yazdırır.
sonuc = yemekTarifi.values() # value bilgileri liste olarak gelir.
sonuc = yemekTarifi.items() #dictionary yapısı bir listeye çevrilir getirilir.

#update items
# yemekTarifi["yemekAdi"] = "mantı" #hem günceller hem ekler
sonuc = yemekTarifi
yemekTarifi.update({"yemekAdi":"mantı"})


#delete items
# yemekTarifi.pop("yemekAdi")
# sonuc = yemekTarifi
yemekTarifi.popitem() #son elemanı siler.
yemekTarifi.clear() #herşeyi siler.
sonuc = yemekTarifi
print(sonuc)

