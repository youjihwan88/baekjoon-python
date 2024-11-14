import sys
import heapq

n = int(sys.stdin.readline().rstrip())
li = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(li) == 0:
            print("0")
        else:
            print(heapq.heappop(li))
    else:
        heapq.heappush(li, x)
