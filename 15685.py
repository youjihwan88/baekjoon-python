import sys

n = int(sys.stdin.readline().rstrip())

li = [[0] * 101 for _ in range(101)]


for _ in range(n):
    x, y, d, g = map(int, sys.stdin.readline().rstrip().split())
    li_d = [d]
    for _ in range(g):
        for e in reversed(li_d):
            li_d.append((e + 1) % 4)

    nx = x
    ny = y
    li[ny][nx] = 1
    for nd in li_d:
        if nd == 0:
            nx += 1
        elif nd == 1:
            ny -= 1
        elif nd == 2:
            nx -= 1
        elif nd == 3:
            ny += 1
        li[ny][nx] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if li[i][j] == 1 and li[i + 1][j] == 1 and li[i][j + 1] == 1 and li[i + 1][j + 1] == 1:
            cnt += 1

print(cnt)
