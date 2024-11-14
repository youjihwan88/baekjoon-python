import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().rstrip()))
li.reverse()

idx = 0
cnt = 0
while True:
    v = k // li[idx]
    cnt += v
    k -= v * li[idx]

    idx += 1
    if k == 0:
        break

print(cnt)
