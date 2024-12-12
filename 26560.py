import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if s[-1] != ".":
        s += "."

    print(s)
