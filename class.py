# class Insan():
#     def __init__(self, ad,soyad,yas,meslek):
#         self.ad = ad
#         self.soyad = soyad
#         self.yas = yas
#         self.meslek = meslek

#     def bilgiSoyle(self):
#         print("İnsanın bilgileri:")
#         print("Adı Soyadı : {} {}".format(self.ad ,self.soyad))
#         print("Yaşı: {}".format(self.yas))
#         print("Mesleği: {}".format(self.meslek))


# i1 = Insan("edanur","korkmaz",24,"bilgisayar mühendisi")
# i2 = Insan("sude","korkmaz",18,"öğrenci")

# i1.bilgiSoyle()
# i2.bilgiSoyle()

# class Araba():
#     def __init__(self, marka, model, yil, bakim = True):
#         self.marka = marka
#         self.model = model
#         self.yil = yil
#         self.bakim = bakim

#     def ozellikleriGoster(self):
#         print("Arabanın Özellikleri: ")
#         print("markası:{}, modeli: {}, yaşı:{}".format(self.marka,self.model,self.yil,))
#         self.bakimDurumu()

#     def bakimDurumu(self):
#         if self.bakim == True:
#             print("Bakımı Yapıldı.")
#         else:
#             print("Bakım Yapılmadı.")


# a1 = Araba("BMW","5.20",2024)

# a2 = Araba("Mercedes","5.22",2023,False)

# a1.ozellikleriGoster()
# a2.ozellikleriGoster()

class Musteri():
    def __init__(self,musteriNo,ad,soyad,bakiye,hesapTuru):
        self.musteriNo = musteriNo
        self.ad = ad
        self.soyad = soyad
        # self.bakiye = bakiye
        # self.hesapTuru = hesapTuru
        self.Hesap = self.Hesap(bakiye, hesapTuru)
    
    def bilgileriGoster(self):
        print(self.musteriNo,self.ad,self.soyad)
        self.Hesap.bilgileriGoster()

    class Hesap:
        def __init__(self,bakiye,hesapTuru):
            self.bakiye = bakiye
            self.hesapTuru = hesapTuru
        def bilgileriGoster(self):
            print(self.bakiye,self.hesapTuru)
            

m1 = Musteri(1,"eda","korkmaz",5000,"Tl")
m2 = Musteri(2,"sude","korkmaz",7000,"dolar")

m1.bilgileriGoster()
m2.bilgileriGoster()



    
        