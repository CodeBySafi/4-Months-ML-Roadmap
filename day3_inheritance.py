class BaseModel:
    def train_Model(self):
        print("Data is training on model")


class linarRegression(BaseModel):

    def predeict(self):
        print("Model has predectited the result")


s1=linarRegression()
s1.train_Model()
s1.predeict()