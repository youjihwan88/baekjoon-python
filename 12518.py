import sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    s = sys.stdin.readline().rstrip()
    rst = None
    if s[-1] in ["a", "i", "e", "o", "u", "A", "I", "E", "O", "U"]:
        rst = "a queen"
    elif s[-1] in ["y", "Y"]:
        rst = "nobody"
    else:
        rst = "a king"

    print(f"Case #{i+1}: {s} is ruled by {rst}.")
