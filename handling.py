# error handling => hata yönetimi

# try: 
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("y için 0 girilemez.")
# except ValueError:
#     print("x ve y için sayısal değer girmelisiniz.")
while True:
   try: 
     x = int(input("x: "))
     y = int(input("y: "))
     print(x/y)
   except Exception as ex:
    print("yanlış bilgi girdiniz.", ex)
   else:
      break
   finally:
       print("try expect sonlandı.")