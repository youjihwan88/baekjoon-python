import sys

n = int(sys.stdin.readline().rstrip())

li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().rstrip()))

if li[1] / li[0] == li[2] / li[1]:
    step = li[1] // li[0]
    print(li[-1] * step)
elif li[1] - li[0] == li[2] - li[1]:
    step = li[1] - li[0]
    print(li[-1] + step)
