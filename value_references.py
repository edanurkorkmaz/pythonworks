#value types

x, y = 5, 25
x = y
y = 10

print(x,y)
# #x etkilenmedi fakat y 10 olarak değişti.


# #reference types
# a = ["apple","banana"]
# b = ["apple","banana"]

# a = b

# b[0] = "grape"

# print(a, b) # ["grape","banana"] , ["grape","banana"]
# #yapılan bir değişiklik aynı adreste yapıldığından dolayı a ve b ' nin içeriği de aynı olur.

a = ["muz","çilek","kivi"]
b = ["karpuz","kavun","armut"]

b = a
a[0] = "erik"
print(a , b)