#Girilen iki sayıdan hangisi büyüktür?

sayı1 = int(input("1.sayıyı giriniz:"))
sayı2 = int(input("2.sayıyı girin:"))

result = (sayı1 > sayı2)
print(f"sayı1: {sayı1} sayı2: {sayı2} den büyüktür: {result}")
                  
                  
#kullanıcıdan 2 vize(%60) ve final notunu(%40) notunu alıp ortalama hesaplayınız.
#Eğer ortalama 50 ve üstü ise geçti yazdırın.
vize1 = float(input("1.vize notu:"))
vize2 = float(input("2.vize notu:"))

final = float(input("final notunu giriniz:"))

ortalama = (((vize1 + vize2)*0.6) + (final*0.4))/2
print(f'not ortalamanız : {ortalama} ve ders geçme durumu: {ortalama>=50}')

print(ortalama)

#girilen bir sayının tek mi çift mi olduğunu anlayın.

sayi = int(input("sayı:"))
tekcift = (sayi % 2 == 0)
print(f"girilen sayının çift olma durumu: {tekcift}")

#girilen bir sayının negatif pozitif durumunu yazdırın.

sayı = int(input("sayı girin:"))
negatifpozitif = (sayı >= 0)
print(f"sayının poztif olma durumu {negatifpozitif}")

#parola ve email bilgilerini girip doğruluğunu kontrol edin.

email = 'korkmaze101@gmail.com'
password = 'eda123'

girilenemail = (input("mail adresini girin."))
girilenpassword = (input("şifrenizi giriniz."))

isMail= (email == girilenemail)
isPassword =(password == girilenpassword) 

print(f"Girilen mail doğru mu: {isMail} ve parola doğru mu: {isPassword}")
