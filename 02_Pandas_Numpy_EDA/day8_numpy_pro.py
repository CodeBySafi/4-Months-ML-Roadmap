import numpy as np

arr1=np.arange(1,13)
print(arr1)

ml_format=arr1.reshape(-1,1)
print(ml_format)

arr2=np.array([

    [10,20],
    [30,40],
    [50,60]
])

men=np.mean(arr2,axis=0)
print(men)

data=arr2-men
print(data)