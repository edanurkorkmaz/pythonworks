
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = b**2 - 4*a*c

if delta > 0:
    sqrt_delta = delta ** 0.5  
    x1 = (-b + sqrt_delta) / (2*a)
    x2 = (-b - sqrt_delta) / (2*a)
    print("İki reel kök var:", x1, "ve", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Çift bir kök var:", x)
else:
    print("Reel kök yok, karmaşık kökler var.")