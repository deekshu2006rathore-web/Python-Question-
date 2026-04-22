with open("seek_example.txt", "w+") as f:
    f.write("0123456789")
    f.seek(0)
    print(f.read(5))             # "01234"
    # Instead of f.seek(2,1), calculate absolute position
    current_pos = f.tell()       # after read(5) -> position 5
    f.seek(current_pos + 2)      # move to position 7
    print(f.read(3))             # reads "567" (positions 7,8,9)