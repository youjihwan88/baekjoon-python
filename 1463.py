import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
if n == 1:
    print("0")
    sys.exit()

visited = [0] * (n + 1)

s = 1
q = deque()
q.append(s)
visited[s] = 1

while True:
    q_size = len(q)
    for _ in range(q_size):
        x = q.popleft()
        for nx in [x + 1, 2 * x, 3 * x]:
            if nx > n:
                continue
            if visited[nx]:
                continue

            visited[nx] = visited[x] + 1
            q.append(nx)
            if nx == n:
                break
        if nx == n:
            break
    if nx == n:
        break

print(visited[n] - 1)
