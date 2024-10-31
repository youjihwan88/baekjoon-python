import sys
from itertools import combinations

n, m, h = map(int, sys.stdin.readline().rstrip().split())
ladder = [[0] * (n - 1) for _ in range(h)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ladder[a - 1][b - 1] = 1

candidate = []
for i in range(h):
    for j in range(n - 1):
        if ladder[i][j] == 0:
            candidate.append((i, j))


def go():
    for j in range(n):
        loc = j
        for i in range(h):
            if loc < n - 1 and ladder[i][loc] == 1:
                loc += 1
            elif loc - 1 >= 0 and ladder[i][loc - 1] == 1:
                loc -= 1

        if j != loc:
            return False

    return True


b_success = False
for cnt in range(len(candidate) + 1):
    if cnt > 3:
        break

    for _candidates in combinations(candidate, cnt):
        b_bad_candidate = False
        for _candidate in _candidates:
            if _candidate[1] - 1 >= 0 and ladder[_candidate[0]][_candidate[1] - 1] == 1:
                b_bad_candidate = True
                break
            if _candidate[1] + 1 < n - 1 and ladder[_candidate[0]][_candidate[1] + 1] == 1:
                b_bad_candidate = True
                break

            ladder[_candidate[0]][_candidate[1]] = 1

        if not b_bad_candidate:
            rst = go()
            if rst:
                b_success = True
                break

        for _candidate in _candidates:
            ladder[_candidate[0]][_candidate[1]] = 0

    if b_success:
        break

if b_success:
    print(cnt)
else:
    print("-1")
