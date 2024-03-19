numbers = [1 ,10, 5, 16, 4, 9, 10]
letters = ['a' , 'g', 's' , 'b', 'y' , 'a', 's']
val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
#print(val)

numbers[4] = 40
#print(numbers)

numbers.append("49")
numbers.append("59")

numbers.insert(3, 78)

numbers.pop() # silmek için kullanılır.
numbers.remove(10)


print(numbers)