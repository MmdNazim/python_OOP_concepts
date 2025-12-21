                                                                                    #PART-1
"""
Docstring for oop_access_modifier:
----------------------------------
what is access modifier?
-> Access modifiers in Python control the visibility and accessibility of class members (attributes and methods) from outside the class.
They determine whether other classes and objects can access, modify, or inherit a particular member. 

Python provides three types of access modifiers:
-Public Access Modifier
-Protected Access Modifier
-Private Access Modifier


->Public Access Modifier:
-Attributes and method are public by default
-They can be accessed and modified both inside and outside the class
-They are no restrictions on public attributes
-Public access modifier ta use krte pari, (inside class)+(child class)+(outside class)

->Protected Access Modifier:
-Protected access modifier ta usr krte pari, (inside class)+(child class)+(outside class(eikhane use kra jay but recomanded na ❌❌❌❌))  
-Prefixed with a single underscore "_" are protected. eikhane ei underscore diye protected kra hoy.

->Private Access Modifier:
-Prefixed with double underscore "__" are called "Private access modifier"
-Private access modifier ta use krte pari, inside the class e.   [NOTE: private access modifier er dhara outside of class and child class e access kra jay na ❌❌❌❌❌❌❌❌]
"""

#public access modifier:
"""
class Car:
    brand = "toyota"

    def display(self):
        print(f"our brand name is:{self.brand}")       #[eikhane "brand" ke class er inside thekeo access kra jay]

    
class Sedan(Car):

    def DisplayFromChild(self):
        print(f"our brand name is:{self.brand}")
    

obj = Sedan()
print(obj.brand)                            #[eikhane "brand" ke "object " create kre class er outside thekeo access kra jay]
obj.DisplayFromChild()
"""

#Protected Access Modifier: amra kono ekta class er majhe use krte cai and oi class er child class e use krte cai but tachara ar class er baire use krte cai na take protected access modifier bole. 
"""
class Car:
   _brand = "toyota"                  #[eikhane "_brand" ke ei "_" (underscore) er use er dhara protected kra hyeche]


   def display(self):
        print(f"our brand name is:{self._brand}")       #[eikhane "_brand" ke class er inside thekeo access kra jay]


class Sedan(Car):

    def DisplayFromChild(self):
        print(f"our brand name is:{self._brand}")        #[eikhane "_brand" ke child class thekeo access kra jay]
    

obj = Sedan()
print(obj._brand)                            #[eikhane "_brand" ke "object " create kre class er outside thekeo access kra jay, but eivabe protected access modifier theke kra recomanded na(❌❌❌❌). eikhane only warning dibe but atkabe na]
obj.DisplayFromChild()
"""

#Private Access Modifier:

class Car:
   __brand = "toyota"                  #[eikhane "__brand" ke ei "__" (double underscore) er use er dhara private kra hyeche]


   def display(self):
        print(f"our brand name is:{self.__brand}")       #[eikhane "__brand" ke class er inside thekeo access kra jay]


class Sedan(Car):

    def DisplayFromChild(self):
        print(f"our brand name is:{self.__brand}")        #[eikhane "__brand" ke child class thekeo access kra jay]
    


obj = Car()
obj.display()



#obj1 = Sedan()     #[NOTE: eikhane "__brand"/Private kra kono properties ke child class theke access kra jay na.(❌❌❌❌)]
#obj1.DisplayFromChild()



#[NOTE: eikhane "__brand"/Private kra kono properties ke "object " create kre outside of class theke access kra jay na.(❌❌❌❌)]