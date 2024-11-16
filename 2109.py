import sys
import heapq

n = int(sys.stdin.readline().rstrip())
li = []

for _ in range(n):
    p, d = map(int, sys.stdin.readline().rstrip().split())
    li.append((d, p))

li.sort()

rst = []
for i in range(n):
    heapq.heappush(rst, li[i][1])
    if len(rst) > li[i][0]:
        heapq.heappop(rst)

sum = 0
for i in range(len(rst)):
    sum += rst[i]

print(sum)
