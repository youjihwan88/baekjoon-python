import sys
from collections import deque


def bfs(li, here):
    visited = [False] * (n + 1)

    q = deque()
    q.append(here)
    visited[here] = True

    cnt = 1

    while True:
        if len(q) == 0:
            break

        here = q.popleft()

        for there in li[here]:
            if visited[there]:
                continue

            q.append(there)
            visited[there] = True
            cnt += 1

    return cnt


n, m = map(int, sys.stdin.readline().rstrip().split())
li = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    li[b].append(a)


# search
rst = [0] * (n + 1)
for i in range(1, n + 1):
    rst[i] = bfs(li, i)

# calc max idx
_max = max(rst)
for i in range(1, n + 1):
    if rst[i] == _max:
        print(i, end=" ")
