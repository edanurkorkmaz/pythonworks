# Sıralı olmayan diziyi ortadan eşit olarak iki alt diziye ayırır.
# Bu ayırma işlemi, alt diziler en çok iki elemanlı olana kadar devam eder.
# Alt dizileri kendi içinde sıralar.
# Sıralı iki alt diziyi tek bir sıralı dizi olacak şekilde birleştirir.

def birlestir(sol, sag):
     siraliliste = []
     i = k = 0
     while i < len(sol) and k < len(sag):
          if sol[i] < sag[k]:
               siraliliste.append(sol[i])
               i += 1
          else:
               siraliliste.append(sag[k])
               k += 1
     siraliliste += sol[i:]
     siraliliste += sag[k:]
     return siraliliste

def mergeSort(sirasizliste):
     if len(sirasizliste) < 2:
          return sirasizliste
     b = int(len(sirasizliste) / 2)
     return birlestir(mergeSort(sirasizliste[:b]), mergeSort(sirasizliste[b:]))
print(mergeSort([4,1,9,6,3,2,10,7,5,8]))