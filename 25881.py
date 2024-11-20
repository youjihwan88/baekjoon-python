import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x <= 1000:
        print(f"{x} {x*a}")
    else:
        print(f"{x} {1000*a + (x-1000)*b}")
