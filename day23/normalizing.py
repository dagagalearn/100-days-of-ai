import numpy as np

arr = np.array([1,2,3])
normalized_arr = ((arr-np.min(arr))/(np.max(arr)-np.min(arr)))
print(normalized_arr)

# Normalizin an array
