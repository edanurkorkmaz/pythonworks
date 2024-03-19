arabalar= ["Bmw","Mercedes","Opel","Mazda"]

#liste kaç elemanlıdır?
result=(len(arabalar))


# listenin ilk ve son elemanı nedir?
resultIlk = arabalar[0]
resultSon= arabalar[3]

#mazda değerini toyota ile değiştirin.
#arabalar[-1]= "Toyota"
#result = (arabalar)

#mercedes listenin bir elemanımıdır?
#result = "Mercedes" in arabalar
#print(result)

#listenin -2 indeksindeki değer nedir?
#result = arabalar[-2]
#print(result)

# listenin 3 elemanını alın.
#result = arabalar[0:3]
#print(result)

# listenin son 2 elemanı yerine toyota ve renault değerlerini ekleyin.
 
arabalar[-2:] = ["toyota", "renault"]
#print(arabalar)

#listenin üzerine audi ve nissan değerlerini ekleyin.
result= arabalar + ["audi", "nissan"]


#listenin son elemanını silin.
del arabalar[-1] 
result = arabalar
print(result)

#liste elemanlarını tersten yazdırın.
result = arabalar[::-1]
print(result)

# aşağıdaki verileri bir liste içinde saklayın.

#studentA:Yiğit Bilgi 2010, (70,60,70)
#studentB:Sena Turan 1999, (80,80,70)
#studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["Yiğit","Bilgi", 2010,[70,60,70]]
studentB = ["Sena","Turan", 1999,[80,80,70]]
studentC = ["Ahmet","Turan", 1998,[80,70,90]]

result = studentA + studentB + studentC 
#print(result)

# liste elemanlarını ekrana yazdırınız.
result = studentC[3]
print(result)

