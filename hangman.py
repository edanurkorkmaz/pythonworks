import random
liste = ["python","print","random","while","choice"]
kelime = random.choice(liste)
adam = ['''
  +----+
  o    |
 /|\   |
 / \   |
      ---''','''
  +----+
  o    |
 /|\   |
 /     |
      ---''','''
  +----+
  o    |
 /|\   |
       |
      ---''','''  +----+
  o    |
 /|    |
       |
      ---''','''  +----+
  o    |
  |    |
       |
     ---''','''
  +----+
  o    |
       |
       |
      ---''','''
  +----+
       |
       |
       |
      ---''']

dogruHarf = []
yanlısHarf = []
hak=len(adam)

while hak > 0:
    out=""
    for h in kelime:
        if h in dogruHarf:
            out += h
        else:
            out += "_"
    if out == kelime:
        break
    print("kelime:",out)
    print(adam[hak-1])     
    girHarf = input()
    if girHarf in dogruHarf or girHarf in yanlısHarf:
        print(girHarf,"zaten girildi.")
    elif girHarf in kelime:
        print("doğru harf")
        dogruHarf.append(girHarf)
    else:
        print("yanlış harf..")
        hak-=1
        yanlısHarf.append(girHarf)
if hak !=0:
    print("tebrikler kazandınız:",kelime)
else:
    print("maalesef kaybettiniz. kelime:",kelime," idi")





    






