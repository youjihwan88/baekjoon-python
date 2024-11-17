import sys

n = int(sys.stdin.readline().rstrip())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().rstrip().split())))

li.sort()

e = li[0][0] + li[0][1]
prev_e = li[0][0] + li[0][1]

for i in range(1, n):
    if li[i][0] < prev_e:
        e = prev_e + li[i][1]
    else:
        e = li[i][0] + li[i][1]
    prev_e = e

print(e)
