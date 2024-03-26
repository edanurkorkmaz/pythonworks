#Bankamatik Uygulaması:

SadikHesap = {
    
    "ad": "Sadık Turan",
    "hesapNo" : "13245678",
    "bakiye": 3000,
    "ekHesap": 2000
}
AliHesap = {
    
    "ad": "Ali Turan",
    "hesapNo" : "12345678",
    "bakiye": 2000,
    "ekHesap": 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap["ad"]}")
    
    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz.")
        
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if(toplam >= miktar):
            ekHesapKullanimi = input("ek hesap kullanılsın mı (e/h)")
            
            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanilacakMiktar
                print("paranızı alabilirsiniz.")
            else:
                print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} bulunmaktadır.")
        else:
            print("Üzgünüz bakiye yetersiz.")

def bakiyeSorgula(hesap):
    print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} TL bulunmaktadir.Ek hesap limitiniz ise {hesap["ekHesap"]} TL bulunmaktadır.")
                    
paraCek(SadikHesap, 3000)
bakiyeSorgula(SadikHesap)
print("***************")
paraCek(SadikHesap, 1000)
bakiyeSorgula(SadikHesap)