import sys
import heapq

n, k = map(int, sys.stdin.readline().rstrip().split())
li_jewel = []
for i in range(n):
    m, v = map(int, sys.stdin.readline().rstrip().split())
    li_jewel.append((m, v))

li_bag = []
for i in range(k):
    li_bag.append(int(sys.stdin.readline().rstrip()))

li_jewel.sort()
li_bag.sort()

sum_price = 0
tmp = []

for bag in li_bag:
    while li_jewel and li_jewel[0][0] <= bag:
        heapq.heappush(tmp, -li_jewel[0][1])
        heapq.heappop(li_jewel)
    if tmp:
        sum_price -= heapq.heappop(tmp)

print(sum_price)
