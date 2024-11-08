import sys
from itertools import combinations

n, k = map(int, sys.stdin.readline().rstrip().split())

li = []
for _ in range(n):
    s = set(sys.stdin.readline().rstrip())
    val = 0
    for c in s:
        val += 1 << (ord(c) - ord("a"))
    li.append(val)


rst = 0
for c in "antic":
    rst += 1 << (ord(c) - ord("a"))

max_cnt = 0


def search(t, val, start):
    global max_cnt
    if t == k:
        cnt = 0
        for l in li:
            if val | l == val:
                cnt += 1
        max_cnt = max(cnt, max_cnt)
        return

    for i in range(start, 26):
        if val & (1 << i):
            continue
        search(t + 1, val | (1 << i), i + 1)

    return


search(5, rst, 0)
print(max_cnt)
