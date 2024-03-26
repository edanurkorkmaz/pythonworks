#def sayHello(name = "user"):
  #  return "hello "+ name

#msg = sayHello("çınar")
#msg = sayHello("ada")

#print(msg)

#def total(num1, num2):
 #   return num1 + num2

#result = total(10,20)
#result = total(15,20)

#print(result)


#def yasHesapla(dogumYili):
 #   return 2024 - dogumYili

#ageCınar = yasHesapla(2017)
#ageAda = yasHesapla(2010)
#ageSena = yasHesapla(1999)

#print(ageCınar, ageAda, ageSena)

def EmekliligeKacYilKaldi(dogumYili,isim):
    yas = 2024 - dogumYili
    emeklilik= 65 - yas 
    
    if emeklilik > 0:
        print (f"emekliliğinize {emeklilik} yil kaldi.")
    else:
        print("zaten emekli oldunuz.")

EmekliligeKacYilKaldi(2000, "ali")

