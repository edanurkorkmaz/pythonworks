# sayilar = (10,20,30,40,50)

# def toplam(liste):
#     sonuc = 0
#     for i in liste:
#         sonuc += i
#     return sonuc

# def toplam(*args):
#     print(args)
#     print(type(args))
#     sonuc = 0
#     for i in args:
#         sonuc += i
#     return args
# sonuc = toplam(10,20,30,40,50,60)


#kwargs

def display_user(**kwargs):
    # print(type(kwargs))
    # print(kwargs)

    for key,value, in kwargs.items():
        print(f"{key}: {value}")
print("\n")

display_user(username = "edakorkmaz")
display_user(username = "edakorkmaz",email="korkmaze101@gmail.com")
display_user(username = "edakorkmaz",email="korkmaze101@gmail.com" ,country ="türkiye")

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value",key2="value2")
