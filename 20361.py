import sys

n, x, k = map(int, sys.stdin.readline().rstrip().split())
for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == x:
        x = b
    elif b == x:
        x = a

print(x)
