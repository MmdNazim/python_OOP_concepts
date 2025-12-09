"""
What is OOP?
OOP stands for Object-Oriented Programming.

Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
"""

class myClass:
    x = 10
    y = 20
    z = 30

    sum = x + y + z

obj1 = myClass()  #[ekta class e amra multiple object eivabe create krte pari]
print(obj1.x)

obj2 = myClass()
print(obj1.y)

obj3 = myClass()
print(obj1.z)

obj4 = myClass()    #[eivabe ekta oject create kre tar maddhome multiple variable ke access krte pari]
print(obj1.x) 
print(obj1.y)
print(obj1.z)
print(obj1.sum)