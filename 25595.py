import sys

n = int(sys.stdin.readline().rstrip())
li = [[0] * n for _ in range(n)]

loc_2 = []
loc_1 = []


for i in range(n):
    _li = list(map(int, sys.stdin.readline().rstrip().split()))
    li[i] = _li
    for j in range(n):
        if li[i][j] == 2:
            loc_2.append(i + j)
        elif li[i][j] == 1:
            loc_1.append(i + j)

answer = (loc_2[0] + 1) % 2

b_fail = False
for e in loc_1:
    if e % 2 != answer:
        b_fail = True
        break

if b_fail:
    print("Kiriya")
else:
    print("Lena")
