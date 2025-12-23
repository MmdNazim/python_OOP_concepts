"""
Docstring for getter_setter_in_private_properties:
--------------------------------------------------
Getters and Setters are methods used to access and modify class attributes in a controlled manner.

Getter: The getter method is used to retrieve the value of a private attribute. It allows controlled access to the attribute.
Setter: The setter method is used to set or modify the value of a private attribute.
        It allows you to control how the value is updated, enabling validation or modification of the data before it’s actually assigned.

Here is the links that's helps us to understand the details:
------------------------------------------------------------
1.https://python-course.eu/oop/properties-vs-getters-and-setters.php
2.https://www.geeksforgeeks.org/python/getter-and-setter-in-python/
3.https://realpython.com/python-getter-setter/

"""



class CAR:

    __BRAND = "Toyota"     #[NOTE: eikhane "__" double underscore er maddhome private kra hyeche variable ke]

    #Getter create:
    @property              #[NOTE: eikhane ei "@property" decorator dhara bujhanu hyeche je, ei function ta ekta private/protected variable ke access krar jonno bananu hyeche]
    def BRAND(self):
        return self.__BRAND
    
    #Setter create:
    @BRAND.setter           #[NOTE: eikhane je decorator use krlam tar details holo, "@" er pore always variable name hbe "BRAND" orthat je variable majhe amra value set krbo tarpore dot diye "setter" ei keyword ta use krte hbe]
    def BRAND(self, value):
        self.__BRAND = value  

obj = CAR()

"""
#Getter create:
print(obj.BRAND)            #[NOTE: amra jkhn "@property" decorator use kre take "getter" function banay tarpor class er object create kre jkhn oi object er through te function ke call krle amra private vriable/property ke access krte parbo na, tokhn amra object er through te just variabler name ta call krlei hbe and amra vaule ke access krte parbo]
"""

#Setter create:
#set value:
obj.BRAND = "MAZDA"         #[NOTE: eikhane je "BRAND" ke call krlam ta holo ei "setter" er "BRAND" ke and tar majhe new value set krechi]
#get value:
print(obj.BRAND)






