import sys
import copy

n, m, t = map(int, sys.stdin.readline().rstrip().split())

li = [[0] * m for _ in range(n)]
loc = []
for i in range(n):
    li[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(m):
        if li[i][j] == -1:
            loc.append([i, j])


def spread_dust(li):
    new_li = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if li[i][j] > 0:
                neigh_val = li[i][j] // 5
                center_val = li[i][j]

                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ny = dy + i
                    nx = dx + j

                    if ny < 0 or nx < 0 or ny >= n or nx >= m or [ny, nx] in loc:
                        continue

                    new_li[ny][nx] += neigh_val
                    center_val -= neigh_val

                new_li[i][j] += center_val

    return new_li


def spread_wind1(li):
    _y, _x = loc[0]

    for i in range(_y, 0, -1):
        li[i][_x] = li[i - 1][_x]
    li[_y][_x] = 0
    for i in range(0, m - 1, 1):
        li[0][i] = li[0][i + 1]

    for i in range(0, _y, 1):
        li[i][m - 1] = li[i + 1][m - 1]

    for i in range(m - 1, 0, -1):
        li[_y][i] = li[_y][i - 1]

    return


def spread_wind2(li):
    _y, _x = loc[1]

    for i in range(_y, n - 1, 1):
        li[i][_x] = li[i + 1][_x]
    li[_y][_x] = 0
    for i in range(0, m - 1, 1):
        li[n - 1][i] = li[n - 1][i + 1]

    for i in range(n - 1, _y, -1):
        li[i][m - 1] = li[i - 1][m - 1]

    for i in range(m - 1, 0, -1):
        li[_y][i] = li[_y][i - 1]

    return


for _ in range(t):
    li = spread_dust(li)
    spread_wind1(li)
    spread_wind2(li)

sum = 0
for i in range(n):
    for j in range(m):
        sum += li[i][j]
print(sum)
