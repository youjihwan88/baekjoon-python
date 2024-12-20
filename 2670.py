import sys
from itertools import combinations


n = int(sys.stdin.readline().rstrip())
li = [0.0] * n

for i in range(n):
    li[i] = float(sys.stdin.readline().rstrip())

tmp = rst = li[0]
for i in range(1, n):
    if li[i] > tmp * li[i]:
        tmp = li[i]
    else:
        tmp *= li[i]

    rst = max(tmp, rst)

print(f"{rst:.3f}")
