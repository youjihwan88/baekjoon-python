import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li = list(map(int, sys.stdin.readline().rstrip().split()))


def check(val):
    cnt = 0
    tmp = 0
    for i in range(len(li)):
        tmp += li[i]
        if tmp > val:
            cnt += 1
            tmp = li[i]
    cnt += 1

    return cnt


l = max(li)
r = sum(li)
rst = r

while l <= r:
    mid = (l + r) // 2
    cnt = check(mid)
    if cnt <= m:
        rst = min(rst, mid)
        r = mid - 1
    else:
        l = mid + 1

print(rst)
