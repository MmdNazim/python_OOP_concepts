#how to work constructors, here is the description:
"""
class MyClass:
    def __init__(self):       #[NOTE: python e "constructor method" create krte gele always constructor name ta hbe "__init__" and eita fixed python er jonno]
        print("hello i am a constructor")

obj = MyClass()
"""

#constructor without parameter:
"""
class MyClass:

    x = 10
    y = 20

    def __init__(self):       
        sum = self.x + self.y      #[constructor methods e jei build-in parameter "self" ache oita diye class er variable gula access kra jay]
        print(sum)

obj = MyClass()
"""

#constructor with parameter:
"""
class MyClass:

    x = 10
    y = 20

    def __init__(self, a, b):       #[constructor method e eivabe parameter pass krte pari]
        sum = self.x + self.y + a + b
        print(sum)

obj = MyClass(5, 5)         #[constructor methods e jei parameter gula pass krechi tar value gula ei class object er through te assign krte pari]
"""

#instence variable: constructor er  through te jodi new variable dynemically class er vitore add kra hoy tokhn take instance variable bole.
"""
class MyClass:

    x = 10
    y = 20

    def __init__(self, zValue):      #[eikhane variable name ta assign krechi]
        self.z = zValue              #[NOTE: eikhane "self.z" diye bujhanu hyeche je ekta "z" namer variable assign kra hocche jeita MyClass() er under e, then "= zValue" holo parameter er "zValue". Ar ei "zValue" er value hbe class object er through te jei value pathanu hbe oita]
    
    
obj = MyClass(10)  

print(obj.z)
"""

#change class variable using constructor params: ei way te class er assign kra variabler value change kra jay.
"""
class MyClass:

    x = 10
    y = 20

    def __init__(self, zValue, xValue):       #[NOTE: eivabe assign kra value change kra jay]
        self.z = zValue
        self.x = xValue             
    
    
obj = MyClass(10, 50)         #[NOTE: eikhane "x" er new value "50" assign kra hyeche]

print(obj.z)
print(obj.x)
"""

#instance method:
"""
class MyClass:

    x = 10
    y = 20

    def __init__(self, zValue, xValue):       #[NOTE: eivabe assign kra value change kra jay]
        self.z = zValue
        self.x = xValue    

    def addTwo(self):                  #[NOTE:ei jei method create kra hyeche take bola hoy "instance method"]    
        print(self.x + self.y + self.z)       #[NOTE: eikhane joto gula variable dhora hyeche tar majhe jei gula dynemically assign ba instence variable ache ba params er through te change variable ache oi new variabler value gula ashbe, karon shob gula ei method er ager method e assign kra hyeche]    
    
    
obj = MyClass(10, 50)         #[NOTE: eikhane "x" er new value "50" assign kra hyeche]

print(obj.z)
print(obj.x)

obj.addTwo() 
"""












