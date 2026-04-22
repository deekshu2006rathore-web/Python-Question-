# Q13: Tuple operations
tup = (1, 2, 3, 4, 5)
print(f"Tuple: {tup}")
print(f"Length: {len(tup)}")
print(f"Index of 3: {tup.index(3)}")
print(f"Count of 2: {tup.count(2)}")

# Immutability demo
try:
    tup[0] = 99
except TypeError as e:
    print(f"Immutability demo: {e}")