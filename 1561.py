import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li = list(map(int, sys.stdin.readline().rstrip().split()))


def check(val):
    cnt1 = 0
    cnt2 = 0
    for e in li:
        if val % e == 0:
            cnt1 = cnt1 + (val // e)
            cnt2 += 1
        else:
            cnt1 = cnt1 + (val // e) + 1
    cnt2 += cnt1

    if cnt1 < n <= cnt2:
        cnt = 0
        for i in range(len(li)):
            if val % li[i] == 0:
                cnt += 1
                if cnt == n - cnt1:
                    return i + 1
    elif n <= cnt1:
        return -1
    elif n > cnt2:
        return -2


l = 0
r = 30 * n // m + 1

while l <= r:
    mid = (l + r) // 2
    val = check(mid)
    if val >= 0:
        rst = val
        break
    elif val == -1:
        r = mid - 1
    elif val == -2:
        l = mid + 1

print(rst)
