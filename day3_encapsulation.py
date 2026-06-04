class ML_Model:
    def __init__(self):
        self.__accuracy=95

    def get_accuracy(self):
        return self.__accuracy
s1=ML_Model()
print(s1.get_accuracy())