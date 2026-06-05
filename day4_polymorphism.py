class shape:
    def __init__(self,name):
        self.name=name
        print("The name of shape is :",self.name)

    def calculate_Area(self):
        pass

class rectangle(shape):
    def __init__(self, name,length,width):
        super().__init__(name)
        self.length=length
        self.width=width

    def calculate_Area(self):
        total= self.length*self.width
        return total
    

class circle(shape):
    def __init__(self, name,radius):
        super().__init__(name)
        self.radius=radius

    def calculate_Area(self):
        total=3.14*self.radius**2
        return total    

s1=rectangle("Rectangle",10,5)
print("Its area is :",s1.calculate_Area())
print("")
R1=circle("Circle",10)
print("Its area is :",R1.calculate_Area())
print("")
obj=[s1,R1]
for i in obj:
    print(i.calculate_Area())
        
        
        
        
