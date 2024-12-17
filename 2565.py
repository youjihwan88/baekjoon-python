import sys
import bisect

n = int(sys.stdin.readline().rstrip())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().rstrip().split())))
li.sort()

li_y = [e[1] for e in li]
d = [li_y[0]]

for i in range(n):
    if li_y[i] > d[-1]:
        d.append(li_y[i])
    else:
        idx = bisect.bisect_left(d, li_y[i])
        d[idx] = li_y[i]

print(n - len(d))
