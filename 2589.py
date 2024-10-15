import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
_map = []
land_li = []
for i in range(n):
    _map.append(sys.stdin.readline().rstrip())
    for j in range(m):
        if _map[i][j] == "L":
            land_li.append((i, j))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

_max = 0
for y, x in land_li:
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if _map[ny][nx] == "L" and visited[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    rst = max([max(row) for row in visited])
    _max = max(_max, rst)


print(_max - 1)
