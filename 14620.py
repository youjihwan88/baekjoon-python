import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
li = [[0] * n for _ in range(n)]

min_cost = 0
for i in range(n):
    li[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        min_cost += li[i][j]

candidates = [(i, j) for i in range(1, n - 1) for j in range(1, n - 1)]


for _candidates in combinations(candidates, 3):
    c1 = _candidates[0]
    c2 = _candidates[1]
    c3 = _candidates[2]

    if abs(c1[0] - c2[0]) ** 2 + abs(c1[1] - c2[1]) ** 2 < 5:
        continue
    if abs(c2[0] - c3[0]) ** 2 + abs(c2[1] - c3[1]) ** 2 < 5:
        continue
    if abs(c3[0] - c1[0]) ** 2 + abs(c3[1] - c1[1]) ** 2 < 5:
        continue

    cost = 0
    for c in [c1, c2, c3]:
        cost += li[c[0]][c[1]]
        cost += li[c[0] - 1][c[1]]
        cost += li[c[0] + 1][c[1]]
        cost += li[c[0]][c[1] - 1]
        cost += li[c[0]][c[1] + 1]

    min_cost = min(cost, min_cost)

print(min_cost)
