src = "source.txt"
dst = "dest.txt"

# Create source file
with open(src, "w") as f:
    f.write("Content to copy\n")

# Copy
with open(src, "r") as fsrc:
    with open(dst, "w") as fdst:
        fdst.write(fsrc.read())

print(f"Copied from {src} to {dst}")