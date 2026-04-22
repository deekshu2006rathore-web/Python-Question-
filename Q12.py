lst = [10, 20, 30, 40, 50, 60]
print(f"Original list: {lst}")
print(f"Slicing [1:4]: {lst[1:4]}")
print(f"Slicing [::2]: {lst[::2]}")

# Manipulation
lst.append(70)
lst.insert(2, 25)
lst.remove(40)
print(f"After append, insert, remove: {lst}")