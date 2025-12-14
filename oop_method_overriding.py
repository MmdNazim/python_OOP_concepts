"""
Docstring for oop_overriding:
Method overriding is a fundamental concept in object-oriented programming (OOP) that allows you to redefine a method in a subclass when that method was already defined in the base class.

Key features and advantage of Method Overriding:
-> Method Overriding is derived from the concept of object oriented programming
-> Method Overriding allows us to change the implementation of a function in the child class which is defined in the parent class.
-> Method Overriding is a part of the inheritance mechanism
-> Method Overriding avoids duplication of code
-> Method Overriding also enhances the code adding some additional properties.


Prerequisites for method overriding:
-> Method overriding cannot be done within a class. So,we need to derive a child class from a parent class. Hence Inheritance is mandatory.
-> The method must have the same name as in the parent class
-> The method must have the same number of parameters as in the parent class.
"""


class Father:
        x = 10
        y = 30
            
        def add(self):
              print(self.x + self.y)  

      
class Son(Father):
       
       #Method_Overriding:
       def add(self):
             print(self.x + self.y + 40)  
     


obj = Son()
obj.add()