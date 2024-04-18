import random

liste = ["taş", "kağıt", "makas"]
pc = random.choice(liste)
player = input("[taş-kağıt-makas]: ").strip().lower() 

print("Bilgisayar", pc, "seçti.")
print("Sen", player, "seçtin.")

if pc == player:
    print("Berabere")
elif (pc == "kağıt" and player == "taş") or (pc == "taş" and player == "makas") or (pc == "makas" and player == "kağıt"):
    print("Kaybettin")
elif (pc == "kağıt" and player == "makas") or (pc == "taş" and player == "kağıt") or (pc == "makas" and player == "taş"):
    print("Kazandın")
else:
    print("Geçersiz giriş yaptınız.")
