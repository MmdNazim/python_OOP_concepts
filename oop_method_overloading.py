"""
Docstring for oop_method_overloading:
-------------------------------------
What is function/method overloading in Python?
As the name suggests, function overloading is the process where the same function can be used multiple times by passing a different number of parameters as arguments. 
But Python does not support function overloading. An error gets thrown if we implement the function overloading code the way we do in other languages. 
The reason is as Python does not have a data type for method parameters.
"""

#method overloading using default arguments:
"""
class Father:
        x = 10
        y = 30
            
        def add(self, a = 0, b = 0):              #[NOTE: eikhane default arguments/optional parameter use kre "method overloading" kra hyeche]
              print(self.x + self.y + a + b)  


obj = Father()
obj.add()
obj.add(10)
obj.add(10, 10)
"""

#method overloading using variable-length arguments:

class Father:
        x = 10
        y = 30

        """   
        def add(self, a = 0, b = 0):              #[NOTE: eikhane default arguments/optional parameter use kre "method overloading" kra hyeche]
              print(self.x + self.y + a + b)
        """


        def myMethod(self, *a):                   #[NOTE: eikhane "variable-length" use kre "method overloading" kra hyeche, Ar ei variable-length declar kra hyeche "*a" diye. ar ei variable-length er moddhe diye joto khushi value pass kra jabe]
               print(a)  

obj = Father()

"""
#add() Result:
obj.add()
obj.add(10)
obj.add(10, 10)
"""

#myMethod() Result:
obj.myMethod()
obj.myMethod(1)
obj.myMethod(1,2)
obj.myMethod(1,2,3,4)
