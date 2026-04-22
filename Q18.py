with open("data.txt", "w") as f:
    f.write("First line\n")

# Append
with open("data.txt", "a") as f:
    f.write("Appended line\n")

# Verify
with open("data.txt", "r") as f:
    print(f.read())