import sys
import heapq

n = int(sys.stdin.readline().rstrip())
li = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(li) == 0:
            print(0)
        else:
            a, b = heapq.heappop(li)
            print(a * b)
    else:
        heapq.heappush(li, [abs(x), 1 if x > 0 else -1])
