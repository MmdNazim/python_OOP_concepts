class myClass:
    x = 10
    y = 20
    z = 30
    

    def addTwo(self,a,b):       #[wikhane "self" parameter ta mendatory, ei "self" parameter diye ek e class er joto gula variables ba resource ache shob gula ke access kra jabe]
                                #[eikhane "self" parameter er pore eksathe aro parameter pathanu jay]
        sum = self.x+self.y+self.z+a+b
        print(sum)

    def addNew(self):
        self.addTwo(20,40)       #[eikhane ekta class er bitore ekta function diye arekta function ke call kranu hyeche]

obj = myClass()

obj.addTwo(40,50)     #[eikhane "addTwo" methods er parameters er value assign kra holo]

obj.addNew()