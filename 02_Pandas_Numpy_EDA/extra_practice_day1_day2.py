import numpy as np
stats = np.array([[45, 80], [55, 95], [30, 40], [90, 85], [20, 25]])
print(np.average(stats,axis=1))
print(np.max(stats,axis=0))
print(np.argmin(stats,axis=0))

import pandas as pd
library_records = {
    "Book_ID": [1001, 1002, 1003, 1004, 1005],
    "Title": ["Python Basics", "Advanced SQL", "ML Intro", "C++ Deep Dive", "Data Logic"],
    "Category": ["Programming", "Database", "AI", "Programming", "Hardware"],
    "Times_Issued": [45, 80, 20, 60, 15]
}

data =pd.DataFrame(library_records)
print(data)

print(data.shape)
print(data.columns)

print(data.head(2))