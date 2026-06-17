class logic_gates:
    def __init__(self,name):
        self.name=name
        print(self.name)


class AND_Gate(logic_gates):
    def __init__(self,name):
        super().__init__(name)
        self.__input_1=None
        self.__input_2=None

    def set_input(self,a,b):
        if a==1 or a==0:
            self.__input_1=a
        else:
            print("Enter 0 or 1 .")

        if b==1 or b==0:
            self.__input_2=b
        else:
            print("Enter 0 or 1")

    def get_output(self):
        if self.__input_1==1 and self.__input_2 ==1:
            return 1
        else:
            return 0
        

class OR_Gate(logic_gates):
    def __init__(self,name):
        super().__init__(name)
        self.__input_1=None
        self.__input_2=None

    def set_input(self,a,b):
        if a==1 or a==0:
            self.__input_1=a
        else:
            print("Enter 0 or 1 .")

        if b==1 or b==0:
            self.__input_2=b
        else:
            print("Enter 0 or 1")

    def get_output(self):
        if self.__input_1==1 or self.__input_2 ==1:
            return 1
        else:
            return 0

s1=AND_Gate("AND GATE")
s1.set_input(1,0)
print("OUTPUT",s1.get_output())
print("")
A1=OR_Gate("OR GATE")
A1.set_input(1,0)
print("OUTPUT:",A1.get_output())
print("")
A2=OR_Gate("OR GATE")
A2.set_input(3,6)
print("OUTPUT :",A2.get_output())

