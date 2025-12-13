#when parent class has constructor, but the child class has no constructor:
"""
class Father:
    x = 10
    y = 30


    def add(self):
        print(self.x + self.y)

    def __init__(self):                       
        print("father constructor")


class Son(Father):                             #[NOTE: "father()" class er jei constructor ta ache oita inheritancer karone "son()" class ta access krte parbe] 
    pass


obj = Father()
obj = Son()
"""

#when child class has constructor, but the parent class has no constructor:
"""
class Father:
    x = 10
    y = 30


    def add(self):
        print(self.x + self.y)


class Son(Father):                             #[NOTE: "son()" class er jei constructor ta ache oita khali "son()" class e access krte parbe, karon inheritance ruels "up to buttom "kaj kre tai "son()" class er constructor ke "father()" class access krte parbe na] 

        def __init__(self):                       
         print("son constructor")
    


obj = Father()
obj = Son()
"""

#when parent and child both class has constructor:
"""
class Father:
    x = 10
    y = 30

    def __init__(self):                       
        print("father constructor")


    def add(self):
        print(self.x + self.y)



      
class Son(Father):                            #[NOTE: "son()" class and "father()" class er jodi alada alada constructor thake then "father()" class ar "son()" class er object create krar pore tara tader nijeder constructor use kre/call kre] 
        
        def __init__(self):                       
         print("son constructor")
    

obj = Father()
obj = Son()
"""

#parent and child both class has constructor, now child class accessing the parent's class constructor:  

class Father:
    x = 10
    y = 30

    def __init__(self):                       
        print("father constructor")


    def add(self):
        print(self.x + self.y)



      
class Son(Father):                          
        
        def __init__(self):
         super().__init__()                 #[NOTE: "son()" class tar "father()" class er constructor ke eivabe "supper()" method er maddhome access krte pare]                    
         print("son constructor")
    

obj = Son()
