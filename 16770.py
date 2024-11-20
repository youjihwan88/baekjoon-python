import sys

n = int(sys.stdin.readline().rstrip())
li = [0] * 1001
for _ in range(n):
    s, t, b = map(int, sys.stdin.readline().rstrip().split())
    for i in range(s, t + 1):
        li[i] += b

print(max(li))
