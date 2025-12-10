#static method:
"""
#Decorators in Python:
In Python, decorators are flexible way to modify or extend behavior of functions or methods, without changing their actual code.

->A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
->Decorators are often used in scenarios such as logging, authentication and memorization,
  allowing us to add additional functionality to existing functions or methods in a clean, reusable way.
"""

class MyClass():
    x = 10
    y = 30

    @staticmethod     #[eikhane ei "decorator function" ke use kre class method ke static method kra hyeche]
    def addTwo():
        z = MyClass.x + MyClass.y
        print(z)

MyClass.addTwo()        #[eikhane class diye static method ke dhorte perechi]

obj = MyClass()
obj.addTwo()      #[eikhane object create kre ei method ke dhora hyeche]


#static variable:


class MyClass():
    x = 10
    y = 30

    @staticmethod     #[eikhane ei "decorator function" ke use kre class method ke static method kra hyeche]
    def addTwo():
        z = MyClass.x + MyClass.y
        print(z)

print(MyClass.x)      #[eivabe class diye variable access kra jay ar ei access krar way ke bola hoy static variable]
print(MyClass.y)


obj = MyClass()       #[eivabe class er object create kre class variable ke access kra jay]
print(obj.x)
print(obj.y)