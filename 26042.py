import sys

n = int(sys.stdin.readline().rstrip())

cnt = 0
max_cnt = 0
min_val = 100000
for _ in range(n):
    li_in = list(map(int, sys.stdin.readline().rstrip().split()))

    if li_in[0] == 1:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            min_val = li_in[1]
        elif cnt == max_cnt:
            min_val = min(min_val, li_in[1])

    elif li_in[0] == 2:
        cnt -= 1

print(f"{max_cnt} {min_val}")
