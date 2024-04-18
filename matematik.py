import random 

print("10 soruluk bir çarpım tablosu testi")
skor = 0
for a in range(10):
    i = random.randint(1, 10)
    x = random.randint(1, 10)
    soru = "{}*{}=".format(i, x)

    dCvp = i * x
    cvp = input(soru)
    cvp = int(cvp)

    if cvp == dCvp:
        skor += 1

if skor > 8:
    print("pekiyi")
elif skor > 6:
    print("iyi")
elif skor > 4:
    print("orta")
else:
    print("daha çok çalışmalısın.")
