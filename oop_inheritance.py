#Inheritance details:
"""
Python Inheritance:

-> Inheritance allows us to define a class that inherits all the methods and properties from another class.

-> Parent class is the class being inherited from, also called base class.

-> Child class is the class that inherits from another class, also called derived class.
---------------------------------------------------------------------------------------------------------------->
-> Inheritance in object-oriented programming (OOP) allows a new class (child or subclass) to inherit attributes and methods from an existing class (parent or superclass). 
This promotes code reusability and modularity, representing an "is-a" relationship. 

-> Key concepts include:
Code Reusability: Attributes and behaviors are defined once in the parent class.
Extensibility: Child classes can add new attributes/methods or modify (override) inherited ones.
super() Function: Used to access parent class elements from the child class.
Method Resolution Order (MRO): Determines the search order in multiple inheritance. 

-> Python supports five main types of inheritance: Single, Multiple, Multilevel, Hierarchical, and Hybrid. 
"""



#single inheritance:
"""
class Father():
    x = 10
    y = 20


    def sub(self):
        print(self.x - self.y)

    
    def add(self):
        print(self.x + self.y)

    def mul(self):
        print(self.x * self.y)

    


class Son(Father):       #[NOTE: eikhane "Father" ke iheritance krche "Son"]
    pass


obj = Son()

# obj = Father()      #[NOTE: "Father" class tar nijer attributes and method ke "Father" object er through te dhorte pare]

obj.sub()
obj.add()
obj.mul()

print(obj.x)
print(obj.y)
"""

#multiple inheritance:
"""
class Father():
    x = 10
    y = 20


    def sub(self):
        print(self.x - self.y)

    
    def add(self):
        print(self.x + self.y)



class Mother():
    a = 100
    b = 200

    def mul(self):
        print(self.a * self.b)

    def div(self):
        print(self.a * self.b)


class Son(Father, Mother):       #[NOTE: eikhane "Father" and "Mother"  ke iheritance krche "Son" diye, ar ei inheritance ke bola hoy multiple inheritance]
    pass


obj = Son()

#father ke access kre pacche:
print(obj.x)
print(obj.y)
obj.add()
obj.sub()

#mother ke access kre pacche:
print(obj.a)
print(obj.b)
obj.mul()
obj.div()
"""

#multilevel inheritance:

class GrandFather():
    x = 10
    y = 20


    def sub(self):
        print(self.x - self.y)

    
    def add(self):
        print(self.x + self.y)

class Father(GrandFather):      #[NOTE: eikhane multilevel er inheritance create hyeche, multilevel sequence: "grandfather -> father"]
    pass

class Son(Father):              #[NOTE: eikhane multilevel er inheritance create hyeche, multilevel sequence: "father -> son"]
    pass 


obj = GrandFather()          
print(obj.x)
print(obj.y)
obj.add()
obj.sub()

obj = Father()
print(obj.x)
print(obj.y)
obj.add()
obj.sub()

obj = Son()            #[NOTE: ei "son()" class ta "grandfather" class er shob property, attributes and method access krte parche because of multilevel inheritance, grandfather -> father -> son] 
print(obj.x)
print(obj.y)
obj.add()
obj.sub()
