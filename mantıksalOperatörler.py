#girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz. 
#sayi = float(input("sayı giriniz:"))

#result = (sayi > 0) and (sayi <= 100)
#print(f"sayı 0 ile 100 arasında mı {result}")

#girilen bir sayının pozitif çift sayı olup olmadığını kontrol edin.
#sayi = float(input("sayı giriniz:"))
#result = (sayi > 0) and (sayi % 2 ==0)
#print(f"girilen sayı pozitif çift sayı mı {result}")

#email ve parola bilgileri ile giriş kontrolü yapınız.

#email = 'korkmaze101@gmail.com'
#password = 'eda123'

#girilenemail = (input("mail adresini girin."))
#girilenpassword = (input("şifrenizi giriniz."))

#result = (email == girilenemail) and (password == girilenpassword) 
#print(f"uygulamaya giriş başarılı mı {result}")

#girilen 3 sayıyı büyüklük olarak karşılaştırınız.

#a = int(input("a: "))
#b = int(input("b: "))
#c = int(input("c: "))

#result = (a > b) and (a > c )
#print(f"a en büyük sayıdır. {result}")

#result = (b > a) and (b > c )
#print(f"b en büyük sayıdır. {result}")

#result = (c > a) and (c > b )
#print(f"c en büyük sayıdır. {result}")

#Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. 
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#Finalden 70 alındığında ortalamanın önemi olmasın.

#vize1 = float(input("1.vize notu:"))
#vize2 = float(input("2.vize notu:"))

#final = float(input("final notunu giriniz:"))

#ortalama = (((vize1 + vize2)*0.6) + (final*0.4))/2
#result = (ortalama >= 50) and (final > 50)
#result = (ortalama >= 50) or (final > 70)
#print(f'not ortalamanız : {ortalama} ve ders geçme durumu: {result}')

#Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız. 
# Formül: (Kilo / boy uzunluğunun karesi)
#Aşağıdaki tabloya göre kişi hangi gruba girmektedir.

#0-18.4 => Zayıf
#18.5-24.9 => Normal
#25.0-29.9 => Fazla Kilolu
#30.0-34.9 => Şişman (Obez)

name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)

zayif = (index >= 0) and (index<=18.4)
normal = (index>18.4) and (index<=24.9)
kilolu = (index>24.9) and (index<=29.9)
obez = (index>=29.9) and (index<=34.9)

print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')


