import sys

n = int(sys.stdin.readline().rstrip())
li = []
for i in range(n):
    li.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
li.sort()

idx = len(li) - 1
cnt = 0
b_end = False
while True:
    x = li[idx][0]
    cnt += 1

    while True:
        idx -= 1
        if idx < 0:
            b_end = True
            break
        if li[idx][1] <= x:
            break

    if b_end:
        break
print(cnt)
