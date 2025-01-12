import sys

r, c = map(int, sys.stdin.readline().rstrip().split())
li = [[] for _ in range(r)]
rst = [[0] * c for _ in range(r)]

for i in range(r):
    li[i] = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(r):
    for j in range(c):
        if i == 0 or i == r - 1 or j == 0 or j == c - 1:
            continue

        val = li[i][j]
        if li[i - 1][j] > val and li[i + 1][j] > val and li[i][j - 1] > val and li[i][j + 1] > val:
            rst[i][j] = 1

for i in range(r):
    print(*rst[i], sep=" ")
