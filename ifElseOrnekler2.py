#Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayan 
# python uygulamasını yapınız. Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

#vize1 = float(input('vize 1: '))
#vize2 = float(input('vize 2: '))
#final = float(input('final : '))

#ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)

#result = (ortalama>=50) and (final>=50)
#result = (ortalama >=50) or (final>=70)

#if (ortalama>=50):
#     if (final>=50):
 #         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
  #   else:
   #       print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız. Finalden en az 50 almalısınız.')
#else:
 #    print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')

 #--------------------------------------------------------------------------------
 
 #Finalden 70 alındığında ortalamanın önemi olmasın.
 
#vize1 = float(input('vize 1: '))
#vize2 = float(input('vize 2: '))
#final = float(input('final : '))

#ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)

#result = (ortalama>=50) and (final>=50)
#result = (ortalama >=50) or (final>=70)

#if (ortalama >=50):
   # print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
#else:
  #  if (final>=70):
   #     print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı.Finalden en az 70 aldığınız için geçtiniz.')
   # else:
    #    print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')
        
#Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayan python uygulamasını yapınız.
#Formül: (Kilo / boy uzunluğunun karesi)

#Aşağıdaki tabloya göre kişi hangi gruba girmektedir.

#0-18.4 => Zayıf
#18.5-24.9 => Normal
#25.0-29.9 => Fazla Kilolu
#30.0-34.9 => Şişman (Obez)

name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)

if (index >= 0) and (index<=18.4):
   print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf.')
elif (index>18.4) and (index<=24.9):
   print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal.')
elif (index>24.9) and (index<=29.9):
   print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu.')
elif (index>=29.9) and (index<=45.9):
   print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez.')
else:
   print('bilgileriniz yanlış.')