import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li_1 = list(map(int, sys.stdin.readline().rstrip().split()))
li_2 = list(map(int, sys.stdin.readline().rstrip().split()))


max_score = 0
for i in range(m):
    if i >= n:
        max_score = max(max_score, li_2[i])
    else:
        max_score = max(max_score, li_2[i] - li_1[i])

print(max_score)
