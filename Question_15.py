#Given a 2D NumPy array a = np.array([[45, 60], [30, 80]]), replace all values greater than 50 with 100 and calculate the mean of each column.
import numpy as np
a=np.array([[45,60],[30,80]])
a[a>50]=100
print(a)
print(a.mean(axis=0))