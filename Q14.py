# Q14: Dict add, update, delete
d = {"name": "John", "age": 25}
print(f"Original: {d}")

# Add
d["city"] = "New York"
print(f"After add: {d}")

# Update
d["age"] = 26
print(f"After update: {d}")

# Delete
del d["city"]
print(f"After delete: {d}")