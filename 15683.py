import sys
from itertools import product
from copy import deepcopy

n, m = map(int, sys.stdin.readline().rstrip().split())
li = [[0] * m for _ in range(n)]

cctv_li = []  # cctv_num, y, x, dir
for i in range(n):
    _li = list(map(int, sys.stdin.readline().rstrip().split()))
    li[i] = _li
    for j in range(m):
        if li[i][j] == 1:
            cctv_li.append([[1, i, j, 0], [1, i, j, 1], [1, i, j, 2], [1, i, j, 3]])
        elif li[i][j] == 2:
            cctv_li.append([[2, i, j, 0], [2, i, j, 1]])
        elif li[i][j] == 3:
            cctv_li.append([[3, i, j, 0], [3, i, j, 1], [3, i, j, 2], [3, i, j, 3]])
        elif li[i][j] == 4:
            cctv_li.append([[4, i, j, 0], [4, i, j, 1], [4, i, j, 2], [4, i, j, 3]])
        elif li[i][j] == 5:
            cctv_li.append([[5, i, j, 0]])


def check(_map, y, x, dir):
    if dir == 0:
        for i in range(x + 1, m):
            if _map[y][i] == 6:
                break
            _map[y][i] = -1
    elif dir == 1:
        for i in range(y - 1, -1, -1):
            if _map[i][x] == 6:
                break
            _map[i][x] = -1
    elif dir == 2:
        for i in range(x - 1, -1, -1):
            if _map[y][i] == 6:
                break
            _map[y][i] = -1
    elif dir == 3:
        for i in range(y + 1, n):
            if _map[i][x] == 6:
                break
            _map[i][x] = -1

    return


min_cnt = m * n
for _samples in product(*cctv_li):
    _map = deepcopy(li)

    for _s in _samples:
        num = _s[0]
        y = _s[1]
        x = _s[2]
        dir = _s[3]

        if num == 1 and dir == 0:
            check(_map, y, x, 0)
        elif num == 1 and dir == 1:
            check(_map, y, x, 1)
        elif num == 1 and dir == 2:
            check(_map, y, x, 2)
        elif num == 1 and dir == 3:
            check(_map, y, x, 3)
        elif num == 2 and dir == 0:
            check(_map, y, x, 0)
            check(_map, y, x, 2)
        elif num == 2 and dir == 1:
            check(_map, y, x, 1)
            check(_map, y, x, 3)
        elif num == 3 and dir == 0:
            check(_map, y, x, 0)
            check(_map, y, x, 1)
        elif num == 3 and dir == 1:
            check(_map, y, x, 1)
            check(_map, y, x, 2)
        elif num == 3 and dir == 2:
            check(_map, y, x, 2)
            check(_map, y, x, 3)
        elif num == 3 and dir == 3:
            check(_map, y, x, 3)
            check(_map, y, x, 0)
        elif num == 4 and dir == 0:
            check(_map, y, x, 0)
            check(_map, y, x, 1)
            check(_map, y, x, 2)
        elif num == 4 and dir == 1:
            check(_map, y, x, 1)
            check(_map, y, x, 2)
            check(_map, y, x, 3)
        elif num == 4 and dir == 2:
            check(_map, y, x, 2)
            check(_map, y, x, 3)
            check(_map, y, x, 0)
        elif num == 4 and dir == 3:
            check(_map, y, x, 3)
            check(_map, y, x, 0)
            check(_map, y, x, 1)
        elif num == 5 and dir == 0:
            check(_map, y, x, 0)
            check(_map, y, x, 1)
            check(_map, y, x, 2)
            check(_map, y, x, 3)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if _map[i][j] == 0:
                cnt += 1

    min_cnt = min(min_cnt, cnt)

print(min_cnt)
