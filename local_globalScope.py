# x = "global scope"

# def my_func():
#     x = "local scope"
#     print(x)

# my_func()
# print(x)

name = "Çınar"

def change_name(new_name):
   name = new_name
   print(name) 

change_name("eda")
print(name)