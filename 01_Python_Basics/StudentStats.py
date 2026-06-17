class StudentStats:
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks 

    def get_mean(self):
        self.mean=sum(self.marks)/len(self.marks)
        print("The average Marks of :","",self.name ,"is:","",self.mean)

    def get_varience(self):
        total=0
        for i in self.marks:
            total+=(i-self.mean)**2

        varience=(total)/len(self.marks)
        print("The varience of marks is :",varience)

s1=StudentStats("safiullah",[10,20,25,35,30])
s1.get_mean()
s1.get_varience()

