import numpy as np 
arr1=np.array([
    [1,2,3],[4,5,6]
])
print(arr1*10)

arr2=np.array([
    [5,5,5],[5,5,5]
])

print(arr1+arr2)

arr4=np.array([
    [85, 90, 88], [78, 82, 80], [92, 95, 98], [60, 65, 62]
])

print(np.average(arr4,axis=0))
print(np.sum(arr4,axis=1)) 


X=np.array([
    [1,2,3],[1,2,3]
])

W=np.array(
    [
        [1,2],[1,2],[1,2]
    ]
)

print(X@W)