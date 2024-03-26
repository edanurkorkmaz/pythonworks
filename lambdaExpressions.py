#def square(num): return num ** 2

#numbers = [1, 3, 5, 9]

#result = list(map(square, numbers))
#print(result)

############################################################
square = lambda num: num ** 2
numbers = [1, 3, 5, 9]

result = list(map(lambda num:num ** 2, numbers))
result= square(3)
print(result)



