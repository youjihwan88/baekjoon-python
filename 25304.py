import sys

x = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

sum = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    sum += a * b

if sum == x:
    print("Yes")
else:
    print("No")
