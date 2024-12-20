import sys
import bisect


n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))
d = [li[0]]
loc = [[0, 0] for _ in range(n)]

for i in range(n):
    if li[i] > d[-1]:
        d.append(li[i])
        loc[i] = [len(d) - 1, li[i]]
    else:
        idx = bisect.bisect_left(d, li[i])
        d[idx] = li[i]
        loc[i] = [idx, li[i]]


v = len(d) - 1
rst = []
for i in range(len(loc) - 1, -1, -1):
    if loc[i][0] == v:
        rst.append(loc[i][1])
        v -= 1

    if v == -1:
        break

print(len(d))
print(*rst[::-1], sep=" ")
