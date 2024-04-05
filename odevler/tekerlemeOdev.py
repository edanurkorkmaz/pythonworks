file = open("tekerleme.txt","r") 
file = open("C:\Users\Topfiyt3\Desktop\pythonworks\odevler","w")

tekerleme = file.read()
harf = input("Lütfen bir harf girin: ")
kacKere = tekerleme.count(harf)

print(f"'{harf}' harfi metin içinde {kacKere} kez geçiyor.")


file.close()