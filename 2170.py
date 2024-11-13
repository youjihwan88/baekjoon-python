import sys

n = int(sys.stdin.readline().rstrip())
li = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    li.append((x, y))

li.sort()

s = li[0][0]
e = li[0][1]
sum_len = 0
for i in range(len(li) - 1):
    if li[i + 1][0] <= e:
        e = max(e, li[i + 1][1])
    else:
        sum_len += e - s
        s = li[i + 1][0]
        e = li[i + 1][1]

sum_len += e - s
print(sum_len)
