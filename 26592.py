import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a, b = map(float, sys.stdin.readline().rstrip().split())
    rst = a * 2 / b
    print(f"The height of the triangle is {rst:.2f} units")
