import sys
from itertools import product
from copy import deepcopy

n = int(sys.stdin.readline().rstrip())
li = [[0] * n for _ in range(n)]

for i in range(n):
    li[i] = list(map(int, sys.stdin.readline().rstrip().split()))


def move_up(li):
    for i in range(n):
        curr = 0
        prev = 0
        vec = []
        for j in range(n):
            if li[j][i] != 0:
                curr = li[j][i]

                if curr == prev:
                    vec.append(curr * 2)
                    curr = 0
                elif prev != 0:
                    vec.append(prev)

                prev = curr
        if prev != 0:
            vec.append(prev)

        for j in range(n):
            if j < len(vec):
                li[j][i] = vec[j]
            else:
                li[j][i] = 0
    return


def move_down(li):
    for i in range(n):
        curr = 0
        prev = 0
        vec = []
        for j in range(n - 1, -1, -1):
            if li[j][i] != 0:
                curr = li[j][i]

                if curr == prev:
                    vec.append(curr * 2)
                    curr = 0
                elif prev != 0:
                    vec.append(prev)

                prev = curr
        if prev != 0:
            vec.append(prev)

        for j in range(n):
            if j < len(vec):
                li[n - j - 1][i] = vec[j]
            else:
                li[n - j - 1][i] = 0
    return


def move_left(li):
    for i in range(n):
        curr = 0
        prev = 0
        vec = []
        for j in range(n):
            if li[i][j] != 0:
                curr = li[i][j]

                if curr == prev:
                    vec.append(curr * 2)
                    curr = 0
                elif prev != 0:
                    vec.append(prev)

                prev = curr
        if prev != 0:
            vec.append(prev)

        for j in range(n):
            if j < len(vec):
                li[i][j] = vec[j]
            else:
                li[i][j] = 0
    return


def move_right(li):
    for i in range(n):
        curr = 0
        prev = 0
        vec = []
        for j in range(n - 1, -1, -1):
            if li[i][j] != 0:
                curr = li[i][j]

                if curr == prev:
                    vec.append(curr * 2)
                    curr = 0
                elif prev != 0:
                    vec.append(prev)

                prev = curr
        if prev != 0:
            vec.append(prev)

        for j in range(n):
            if j < len(vec):
                li[i][n - j - 1] = vec[j]
            else:
                li[i][n - j - 1] = 0
    return


_max = 0
for p in product(range(4), repeat=5):
    new_li = deepcopy(li)
    for _p in p:
        if _p == 0:
            move_up(new_li)
        elif _p == 1:
            move_down(new_li)
        elif _p == 2:
            move_left(new_li)
        elif _p == 3:
            move_right(new_li)

    for i in range(n):
        for j in range(n):
            _max = max(_max, new_li[i][j])


print(_max)
