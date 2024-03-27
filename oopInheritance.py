class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")
    
    def who_am_i(self):
        print("I am a person")
    
    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("student created")
        
    def who_am_i(self):
        print("I am a student")

p1 = Person("Ali","Yılmaz")
s1 = Student("Çınar","Turan", 1256)

print(p1.firstName +" " + p1.lastName)
print(s1.firstName +" " + s1.lastName+" "+ str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
s1.eat()
p1.eat()