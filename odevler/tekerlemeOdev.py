file = open("tekerleme.txt","r") 
<<<<<<< HEAD
#file = open("C:/Users/Topfiyt3/Desktop/pythonworks/odevler/tekerleme.txt","w")
=======
>>>>>>> c391ffc18917467bb95b7afca50a2a01c7724156

tekerleme = file.read()
harf = input("Lütfen bir harf girin: ")
kacKere = tekerleme.count(harf)

print(f"'{harf}' harfi metin içinde {kacKere} kez geçiyor.")


file.close()