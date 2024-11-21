import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    i -= 1
    j -= 1
    li[i : j + 1] = reversed(li[i : j + 1])

print(*li, sep=" ")
