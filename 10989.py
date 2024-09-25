import sys

n = int(sys.stdin.readline().rstrip())
li = [0] * 10001

for _ in range(n):
    li[int(sys.stdin.readline().rstrip())] += 1

for i, e in enumerate(li):
    for _ in range(e):
        print(i)
