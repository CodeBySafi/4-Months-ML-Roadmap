import numpy as np

sales_matrix = np.array([
    [5000, 3000, 1000],  
    [7000, 2500, 1500],  
    [4000, 4000, 1200]   
])

house_ages = np.array([5, 10, 2, 15, 20, 1, 8, 12])

discount=np.array([500,200,50])
final_sales=sales_matrix-discount
print(final_sales)

ml_ready_ages=house_ages.reshape(-1,1)
print(ml_ready_ages)

print(final_sales.shape)
print(ml_ready_ages.shape)


