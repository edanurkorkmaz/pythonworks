import re
yazılanMailler = []

for i in range(20):
    email = input("Lütfen e-posta adresinizi girin: ")
    dogruMail = "eda"
    
    if dogruMail == email:
        yazılanMailler.append(email)

with open("dogru_emailler.txt", "w") as file:
    for email in yazılanMailler:
        file.write(email + "\n")

