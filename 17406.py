import sys
from itertools import permutations
from copy import deepcopy


def rotate_li(li, r, c, s):
    for i in range(1, s + 1):
        vec = []
        curr = [r - i, c - i, li[r - i][c - i]]

        for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            for _ in range(2 * i):
                vec.append(curr)

                curr = [curr[0] + dy, curr[1] + dx, li[curr[0] + dy][curr[1] + dx]]

        for j in range(len(vec)):
            li[vec[j][0]][vec[j][1]] = vec[(j + len(vec) - 1) % len(vec)][2]

    return


def get_val(li):
    _min = n * m * 100
    for i in range(n):
        _min = min(_min, sum(li[i]))

    return _min


n, m, k = map(int, sys.stdin.readline().rstrip().split())
li = [[0] * m for _ in range(n)]

for i in range(n):
    li[i] = list(map(int, sys.stdin.readline().rstrip().split()))

_all = []
for _ in range(k):
    r, c, s = map(int, sys.stdin.readline().rstrip().split())
    _all.append([r - 1, c - 1, s])

_min = n * m * 100
for _samples in permutations(_all, len(_all)):
    new_li = deepcopy(li)
    for _sample in _samples:
        rotate_li(new_li, _sample[0], _sample[1], _sample[2])

    _min = min(_min, get_val(new_li))

print(_min)
