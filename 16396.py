import sys

n = int(sys.stdin.readline().rstrip())
li = [0] * 10000
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    for i in range(a - 1, b - 1):
        li[i] = 1

print(sum(li))
