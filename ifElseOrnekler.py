# Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol eden 
# python uygulamasını yapınız.
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

#isim = input("Adınız: ")
#yas = int(input("Yaşınız: "))
#egitim = input("eğitim durumunuz: ")

#if(yas >= 18) and (egitim == "lise" or egitim == "üniversite"):
#    print("ehliyet alabilirsiniz.")
 
#else:
#    print("ehliyet alamazsınız.") 
    
#-----------------------------------------------------------------------------------------------    
#Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına 
# karşılık gelen not bilgisini yazdıran python uygulamasını yapınız.
# 0 -24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5
 
#yazılı1 = float(input("yazılı1 notunu giriniz:"))
#yazılı2 = float(input("yazılı2 notunu giriniz:"))
#sözlü = float(input("sözlü notunu giriniz:"))

#ortalama = (yazılı1 + yazılı2 + sözlü)/3

#if (ortalama >= 0) and (ortalama < 25):
 #   print(f"ortalamanız {ortalama} notunuz: 0")
#elif(ortalama >= 25) and (ortalama < 45):
 #   print(f"ortalamanız {ortalama} notunuz: 1")
#elif(ortalama >= 45) and (ortalama < 55):
 #   print(f"ortalamanız {ortalama} notunuz: 2")
#elif(ortalama >= 55) and (ortalama < 70):
 #   print(f"ortalamanız {ortalama} notunuz: 3")
#elif(ortalama >= 70) and (ortalama < 85):
 #   print(f"ortalamanız {ortalama} notunuz: 4")
#elif(ortalama >= 85) and (ortalama <= 100):
 #   print(f"ortalamanız {ortalama} notunuz: 5")
#else:
 #   print("yanlış bilgi girdiniz.")
#---------------------------------------------------------------------------------

#import datetime

#tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
#tarih = tarih.split('/')
#trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

#simdi = datetime.datetime.now()
#fark = simdi - trafigeCikis
#days = fark.days

#if days<=365:
 #    print('1.servis aralığı')
#elif days>365 and days<=365*2:
 #    print('2.servis aralığı')
#elif days>365*2 and days<=365*3:
 #   print('3.servis aralığı')
#else:
#    print('hatalı süre.')
    
#-------------------------------------------------------------------------------

#Girilen bir sayının pozitif çift sayı olup olmadığını kontrol eden python uygulamasını yapınız.

#sayı = int(input("sayı giriniz: "))

#if (sayı > 0):
 #   print("sayı pozitiftir.")
  #  if(sayı % 2 == 0):
   #     print("pozitif çift sayıdır.")
    #else:
     #   print("sayı pozitif fakat tek sayıdır.")
#else:
 #   print("sayı negatif sayıdır.")
 
 #---------------------------------------------------------------------------------------------
 
 # Email ve parola bilgileri ile giriş kontrolü yapınız.
 
#email = "korkmaze101@gmail.com"
#parola ="eda123"

#girilenEmail = input("email giriniz: ")
#girilenParola = input("parola giriniz: ")

#if(girilenEmail != email) and (girilenParola != parola):
 #   print("hatalı bilgiler girdiniz.")
#else:
       
 #if(girilenEmail == email):
  #  if(girilenParola == parola):
   #     print("hoşgeldiniz")
   # else:
  #      print("parola bilgisi yanlış")
 #else:
 #   print("email bilginiz yanlış")
 #--------------------------------------------------------------------------------
 


