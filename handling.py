# error handling => hata yönetimi

# try: 
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("y için 0 girilemez.")
# except ValueError:
#     print("x ve y için sayısal değer girmelisiniz.")
# while True:
#    try: 
#      x = int(input("x: "))
#      y = int(input("y: "))
#      print(x/y)
#    except Exception as ex:
#     print("yanlış bilgi girdiniz.", ex)
#    else:
#       break
#    finally:
#        print("try expect sonlandı.")

def renklendir(text, renk):
    renkler = ("blue","red","white","black","orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalıdır.")
    if type(renk) is not str:
        raise TypeError("renk str tipinde olmalıdır.")
    if renk not in renkler:
        raise ValueError("geçersiz bir renk")

try:
   renklendir("merhaba","green")
   renklendir("selam",5)
   renklendir(5,"red") 

except (TypeError, ValueError) as ex:
   print(ex)
