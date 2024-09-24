import sys

li = [[0] * 15 for _ in range(15)]

for i in range(1, 15):
    li[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        li[i][j] = li[i - 1][j] + li[i][j - 1]

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a = int(sys.stdin.readline().rstrip())
    b = int(sys.stdin.readline().rstrip())

    print(li[a][b])
