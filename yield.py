# def sayilar():
#     yield 1
#     yield 2
#     yield 3
# gen = sayilar()

# print(next(gen))
# print(next(gen)) 
# print(next(gen))  


def ard_arda_sayilar(n):
    for i in range(1, n + 1):
        yield i 

generator = ard_arda_sayilar(5)

print(next(generator))  
print(next(generator))  

for sayi in generator:
    print(sayi) 
