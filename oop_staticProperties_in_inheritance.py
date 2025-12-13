#if parent has static properties, child can access those properties as like parent:
"""
class Father:
    x = 10
    y = 30


    @staticmethod
    def addTwo():
        print(Father.x + Father.y)



      
class Son(Father): 
    pass            
    

Father.addTwo()
Son.addTwo()
"""

# if child has static properties, parent can't access those properties as like child:
"""
class Father:
    pass

      
class Son(Father): 
    x = 10
    y = 30


    @staticmethod
    def addTwo():
        print(Son.x + Son.y)          
    

#Father.addTwo()                    #[NOTE: "son()" class er jei static properties gula ache  khali "son()" class e access krte parbe, karon inheritance ruels "up to buttom "kaj kre tai "son()" class er static properties gula ke "father()" class access krte parbe na]

Son.addTwo()
"""

# how child can access parents static and non-static properties: 

class Father:
        x = 10
        y = 30
            
        def addtwofather(self):
               return self.x + self.y
        #  print(self.x + self.y)  

      
class Son(Father): 
     
     def addtwoson(self):
            sum = self.addtwofather() + 100
            print(sum)
        #   print(self.x + self.y)
     


obj = Son()
obj.addtwoson()

