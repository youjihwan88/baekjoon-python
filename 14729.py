import sys
import heapq

top_seven = [-100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0]
limit_score = min(top_seven)

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    x = -1 * float(sys.stdin.readline().rstrip())
    if x > limit_score:
        heapq.heappop(top_seven)
        heapq.heappush(top_seven, x)
        limit_score = min(top_seven)

top_seven.sort(reverse=True)
for e in top_seven:
    print(f"{-e:.3f}")
