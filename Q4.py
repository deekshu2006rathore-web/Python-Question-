a, b, c = map(int, input("Enter 3 numbers: ").split())

if a > b and a > c:
    print("Largest:", a)
elif b > c:
    print("Largest:", b)
else:
    print("Largest:", c)