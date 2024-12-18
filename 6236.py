import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li = [0] * n
for i in range(n):
    li[i] = int(sys.stdin.readline().rstrip())


def check(val):
    tmp = 0
    cnt = 1
    for e in li:
        tmp += e
        if tmp > val:
            tmp = e
            cnt += 1

    return cnt


l = max(li)
r = sum(li)
rst = r
while l <= r:
    mid = (l + r) // 2

    if check(mid) <= m:
        rst = min(rst, mid)
        r = mid - 1
    else:
        l = mid + 1

print(rst)
