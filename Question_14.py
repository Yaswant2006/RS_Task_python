#Create two 3×3 NumPy arrays with random integers. Write code to check and return a boolean array showing element-wise equality.
import numpy as np
rng=np.random.default_rng()
arr1=rng.integers(low=0,high=100,size=(3,3))
arr2=rng.integers(low=0,high=100,size=(3,3))
temp=(arr1==arr2)
print(temp)
