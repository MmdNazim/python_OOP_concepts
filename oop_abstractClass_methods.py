"""
Docstring for oop_abstractClass_methods:
----------------------------------------
-> What is Abstraction in Python?
Abstraction in Python is a process of handling complexity by hiding unnecessary details and showing only the essential information to the user. 

-> In Python, abstraction can be achieved using Abstract Classes and Abstract Methods:
Abstract Method: An abstract method is a method that is declared but contains no implementation. It is just a placeholder that tells the programmer that this method must be overridden by subclasses.
Abstract Class: A class containing one or more abstract methods is called an abstract class. You cannot create an instance of an abstract class directly.

NOTE: abstract class ready krar rules holo, 1.eikhane kono object create kra jabe na  2.abstract jei class ta ke krbo oita obosshoi inherited class theke access krte  hbe. 

-> jei jei jinish shikhlam eikhane:
What is abstraction?
How to create a abstract class
Abstract class without enforcing any abstract method
Abstract class with enforcing one or more abstract method 
"""

from abc import ABC, abstractmethod  #[NOTE: eikhane "abstractmethod" je decorator ache sheita ei mathay bole dite hbe]
class Bangladesh(ABC):               #[NOTE: eikhane "abc" library theke "ABC" feature dhara inherite kre ei class ke a
    
    @abstractmethod                  #[NOTE: eikhane "@abstractmrthod" decorator ta boshiye diye ei method ta ke "abstract method" kre nite hbe]
    def print10to20(self):
        pass

    @abstractmethod                  #[NOTE: eikhane "@abstractmrthod" decorator ta boshiye diye ei method ta ke "abstract method" kre nite hbe]
    def print20to30(self):
        pass
    
    """
    def print0to10(self):
        for i in range(0, 11):
            print(i)
    """
    
    


class Dhaka(Bangladesh):
    def print10to20(self):           #[NOTE: eikhane parent class er "abstract method" ta child class e implement krte hbe & oikhane joto gula "abstract method" thakuk na keno shob gula e child class er majhe implement krte hbe]
        for i in range(10, 21):      #[NOTE: eikhane child class tar parent class er incomplete kra kaj ta complete krte parbe] 
            print(i)

    def print20to30(self):           #[NOTE: parent class jeivabe rekhe gese oivabei child class e implement/enforce kre rakhte parbe]
        pass

obj = Dhaka()
#obj.print0to10()                      #[NOTE: eikhane child class er through te parent class e jei method ta "abstract method" na oi method keo via child class hye access kra jay]
obj.print10to20()
