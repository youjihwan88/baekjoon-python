import sys
import bisect

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))
d = [li[0]]

for i in range(n):
    if li[i] > d[-1]:
        d.append(li[i])
    else:
        idx = bisect.bisect_left(d, li[i])
        d[idx] = li[i]

print(len(d))
