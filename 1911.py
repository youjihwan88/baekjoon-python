import sys

n, l = map(int, sys.stdin.readline().rstrip().split())

li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().rstrip().split())))

li.sort()

idx = 0
prev_e = 0
sum = 0
while True:
    if idx >= len(li):
        break

    if li[idx][0] >= prev_e:
        s = li[idx][0]
    else:
        s = prev_e
    cnt = (li[idx][1] - s + l - 1) // l
    sum += cnt
    e = s + l * cnt

    idx += 1
    prev_e = e

print(sum)
