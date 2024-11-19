import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li = [i + 1 for i in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    a -= 1
    b -= 1
    tmp = li[a]
    li[a] = li[b]
    li[b] = tmp

print(*li, sep=" ")
