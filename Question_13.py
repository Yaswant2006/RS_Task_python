#Create a 5×5 NumPy array of random integers (1 to 100). Replace all even numbers in the array with 0.
import numpy as np
rng = np.random.default_rng()
arr=rng.integers(low=1, high=101, size=(5,5))
arr[arr&1==0]=0  
print(arr)