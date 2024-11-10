import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li = [0] * n

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    for idx in range(i, j + 1):
        li[idx - 1] = k

print(*li, sep=" ")
