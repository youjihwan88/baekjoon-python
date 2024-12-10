import sys
from copy import deepcopy

n, m, t = map(int, sys.stdin.readline().rstrip().split())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().rstrip().split())))

for _ in range(t):
    x, d, k = map(int, sys.stdin.readline().rstrip().split())
    i = 1
    while True:
        if x * i > n:
            break

        if d == 0:
            new_row = li[x * i - 1][m - k :] + li[x * i - 1][: m - k]
        else:
            new_row = li[x * i - 1][k:] + li[x * i - 1][:k]

        li[x * i - 1] = new_row
        i += 1

    new_li = deepcopy(li)
    b_fail = True
    for i in range(n):
        for j in range(m):
            if li[i][j] == li[i][(j + 1) % m]:
                if li[i][j] is not None:
                    b_fail = False
                new_li[i][j] = None
                new_li[i][(j + 1) % m] = None

            if i == n - 1:
                continue

            if li[i][j] == li[i + 1][j]:
                if li[i][j] is not None:
                    b_fail = False
                new_li[i][j] = None
                new_li[i + 1][j] = None

    if b_fail:
        _mean = 0
        _cnt = 0
        for i in range(n):
            for j in range(m):
                if new_li[i][j] is not None:
                    _mean += new_li[i][j]
                    _cnt += 1
        if _cnt == 0:
            continue

        _mean /= _cnt

        for i in range(n):
            for j in range(m):
                if new_li[i][j] is None:
                    continue
                if new_li[i][j] > _mean:
                    new_li[i][j] -= 1
                elif new_li[i][j] < _mean:
                    new_li[i][j] += 1

    li = new_li

_sum = 0
for i in range(n):
    for j in range(m):
        if li[i][j] is not None:
            _sum += li[i][j]

print(_sum)
