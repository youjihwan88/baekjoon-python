import sys

s, c = map(int, sys.stdin.readline().rstrip().split())
li = [0] * s
for i in range(s):
    li[i] = int(sys.stdin.readline().rstrip())


def check(val):
    cnt = 0
    for e in li:
        cnt += e // val
    return cnt


l = 1
r = max(li)
rst = l

while l <= r:
    mid = (l + r) // 2
    cnt = check(mid)
    if cnt >= c:
        rst = max(rst, mid)
        l = mid + 1
    else:
        r = mid - 1

print(sum(li) - rst * c)
