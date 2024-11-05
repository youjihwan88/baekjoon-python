import sys

n = int(sys.stdin.readline().rstrip())
li = [0] * n
for i in range(n):
    in_data = sys.stdin.readline().rstrip()
    for j in range(n):
        if in_data[j] == "T":
            li[i] += 1 << j


def reverse(s):
    for i in range(n):
        if s & (1 << i):
            li[i] = ~li[i]


def count():
    rst = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if li[j] & (1 << i):
                cnt += 1
        rst += min(cnt, n - cnt)
    return rst


global_rst = n * n
for s in range(1 << n):
    reverse(s)
    global_rst = min(global_rst, count())
    reverse(s)

print(global_rst)
