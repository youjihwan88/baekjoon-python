import sys
from itertools import combinations


n = int(sys.stdin.readline().rstrip())
li = [[0] * n for _ in range(n)]

for i in range(n):
    li[i] = list(map(int, sys.stdin.readline().rstrip().split()))

min_score = 100 * n * n
for i in range(1 << n):
    t1 = []
    t2 = []
    for j in range(n):
        if i & (1 << j):
            t1.append(j)
        else:
            t2.append(j)
    if len(t1) != n // 2:
        continue

    t1_score = 0
    t2_score = 0
    for c1, c2 in combinations(t1, 2):
        t1_score += li[c1][c2]
        t1_score += li[c2][c1]

    for c1, c2 in combinations(t2, 2):
        t2_score += li[c1][c2]
        t2_score += li[c2][c1]

    min_score = min(min_score, abs(t1_score - t2_score))
    if min_score == 0:
        break

print(min_score)
