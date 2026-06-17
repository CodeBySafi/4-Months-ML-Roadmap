class student:
    def __init__(self,name,RollNo,Department):
        self.name =name
        self.RollNo=RollNo
        self.Department=Department

    def showDetails(self):
        print("Your name is:",self.name)
        print("Your RollNo is:",self.RollNo)
        print("Your Department is :",self.Department)

s1=student("safiullah",101,"Computer Science")
s1.showDetails()
print("")
s2=student("talha",102,"Computer Science")
s2.showDetails()