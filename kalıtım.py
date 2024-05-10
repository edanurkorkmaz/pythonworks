class X:
    def metot1(self):
        print("X metot 1")
class Y:
    def metot1(self):
        print("Y metot 1")
class Z:
    def metot1(self):
        print("Z metot 1")
class A(X,Y):
    def metot1(self):
        print("A metot 1")
class B(Y,Z):
    def metot1(self):
        print("B metot 1")
class C(B,A,Z):
    pass

# c1 = C()
# c1.metot1()

print(A.mro())