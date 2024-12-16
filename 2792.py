import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li = [0] * m
for i in range(m):
    li[i] = int(sys.stdin.readline().rstrip())


def check(val):
    cnt = 0
    for i in range(m):
        cnt += li[i] // val
        if li[i] % val != 0:
            cnt += 1

    return n >= cnt


l = 1
r = max(li)

rst = 10**9
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        rst = min(rst, mid)
        r = mid - 1
    else:
        l = mid + 1

print(rst)
