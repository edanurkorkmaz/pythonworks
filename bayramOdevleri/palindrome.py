kelime = input("kelime giriniz: ")

ters = kelime[::-1]

if(kelime == ters):
    print("kelime palindromdur.")
else:
    print("kelime palindrom değildir.")