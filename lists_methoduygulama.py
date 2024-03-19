names = ["Ali", "Yagmur", "Hakan", "Deniz"]
years =[1998, 2000, 1998, 1987]


#cenk ismini listenin başına ekleyin.
#names.append("Cenk")
#print(names)

#sena ismini listenin başına ekleyin.
#names.insert (0,"Sena")
#print (names)

#deniz ismini listeden silin.
#names.pop(3)
#print(names)

#Ali listenin bir elemanı mıdır?
#x = names.count("Ali")
#print(x)

#liste elemanlarını ters çevirin.
#names.reverse()
#years.reverse()
#print(names)
#print(years)

#liste elemanlarını alfabetik olarak sıralayınız.
#names.sort()
#years.sort()
#print(names)
#print(years)

# str = "Chevrolet,Dacia" karakter dizisini listeye çevirin.
#str = 'Chevrolet,Dacia'
#result = str.split(',')
#print(result)


#years dizisinin en büyük ve en küçük elemanı nedir?
#min = min(years)
#max = max(years)
#print(min, max)

#years dizisinde kaç tane 1998 değeri vardır.
#result = years.count(1998)
#print(result)

#years dizisinin tüm elemanlarını silin.
#years.clear()
#print(years)

# kullanıcıdan alacağınız 3 tane marka ismini listede saklayınız.
markalar = []
marka = input("marka : ")
markalar.append(marka)

marka = input("marka : ")
markalar.append(marka)

marka = input("marka : ")
markalar.append(marka)


print(markalar)