import sys

n = int(input())
li = list(map(int, input().split()))

_sum = 0
rst = max(li)
for i in range(n):
    _sum += li[i]
    rst = max(rst, _sum)
    if _sum < 0:
        _sum = 0

print(rst)
