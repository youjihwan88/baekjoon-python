import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

if m >= 200001:
    print(0)
    sys.exit()

li = list(map(int, sys.stdin.readline().rstrip().split()))
li.sort()

s_idx = 0
e_idx = len(li) - 1
rst = 0

while True:
    if s_idx >= e_idx:
        break

    val = li[s_idx] + li[e_idx]

    if val == m:
        rst += 1
        s_idx += 1
        e_idx -= 1
    elif val > m:
        e_idx -= 1
    else:
        s_idx += 1

print(rst)
