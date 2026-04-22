# Create file first
with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3")

# Using read()
with open("sample.txt", "r") as f:
    print("read():", f.read())

# Using readline()
with open("sample.txt", "r") as f:
    print("readline():", f.readline(), end="")

# Using readlines()
with open("sample.txt", "r") as f:
    print("\nreadlines():", f.readlines())