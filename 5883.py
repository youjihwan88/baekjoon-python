import sys

n = int(sys.stdin.readline().rstrip())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().rstrip()))

max_cnt = 0
for i in range(n):
    val = li[i]
    tmp = -1
    cnt = 1
    for j in range(i + 1, n):
        if li[j] == val:
            cnt += 1
        elif li[j] == tmp:
            continue
        elif tmp == -1:
            tmp = li[j]
        else:
            break
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
