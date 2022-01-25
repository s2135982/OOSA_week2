'''
Function to find a minimum value by sorting 
'''
from simpSort import findMin
import numpy as np

new_arr = np.random.random(15)
print(new_arr)

min_val = findMin(new_arr)
print(min_val)

