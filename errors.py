# error => hata

# Error
# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError

# error handling => hata yönetimi

# try:
#  x = int(input("x:"))
#  y = int(input("y:"))
#  print(x / y)
# except ZeroDivisionError:
#  print("y 0 olamaz.")
# except ValueError:
#  print("x ve y sayı olmalıdır.")
while True:
 try:
  x = int(input("x:"))
  y = int(input("y:"))
  print(x / y)
 except(ZeroDivisionError, ValueError) as ex:
  print("x ve y sayı olmalıdır. sıfır olamaz.")
  print(ex)

 else:
  break