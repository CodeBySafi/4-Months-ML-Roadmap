class data__processor:
    def __init__(self,data):
        self.data =data
    def show_data(self):
        print(self.data)

class Descriptive_statistics(data__processor):
    def __init__(self, data):
        self. __operation_count=0
        super().__init__(data)
        

    def calculate_mean(self):
        total=0
        for i in self.data:
            
            
            total+=i
        self.__operation_count+=1
        mean=total/len(self.data)
        print("The Mean is : ",mean)

    def find_MAX_MIN(self):
        maximum=max(self.data)
        print("The Maximum number is :",maximum)

        minimum=min(self.data)
        print("The minimum value in list is :",minimum)
        self.__operation_count+=1

    def get_Operation_count(self):
        return self.__operation_count
    
s1=Descriptive_statistics([15,5,65,100,78,98,101,205,987])
s1.show_data()
s1.calculate_mean()
s1.find_MAX_MIN()
print(s1.get_Operation_count())



