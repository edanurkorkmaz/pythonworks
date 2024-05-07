class Person:
    adresses = " no information"
    def __init__(self, name, year):
       self.name = name
       self.year = year
    
       print("init metodu çalıştı.")

p1 = Person(name = "ali",year = 1990)
p2 = Person(name = "yağmur",year =  1995)

print(f"name: {p1.name} year: {p1.year} adresses: {p1.adresses}")
print(f"name: {p2.name} year: {p2.year} adresses = {p2.adresses}")