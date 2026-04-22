import numpy as np

# 1. Array creation
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)

# 2. Indexing and slicing
print("\nElement at index 2 of arr1:", arr1[2])        # 3
print("Slicing arr1[1:4]:", arr1[1:4])                # [2 3 4]

# 3. Arithmetic operations
print("\nArray addition:", arr1 + arr2)               # [11 22 33 44 55]
print("Array subtraction:", arr2 - arr1)              # [9 18 27 36 45]
print("Array multiplication:", arr1 * arr2)           # [10 40 90 160 250]
print("Array division:", arr2 / arr1)                 # [10.  10.  10.  10.  10.]

# 4. More numpy operations
print("\nSum of arr1:", np.sum(arr1))
print("Mean of arr1:", np.mean(arr1))
print("Max of arr1:", np.max(arr1))
print("Min of arr1:", np.min(arr1))
print("Square root of arr1:", np.sqrt(arr1))