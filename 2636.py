import sys

sys.setrecursionlimit(10**6)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dfs(_map, visited, y, x, li_c):
    visited[y][x] = 1
    _map[y][x] = -1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        if visited[ny][nx] == 0:
            if _map[ny][nx] == 0:
                dfs(_map, visited, ny, nx, li_c)
            elif _map[ny][nx] == 1:
                li_c.append([ny, nx])
                visited[ny][nx] = 1


n, m = map(int, sys.stdin.readline().rstrip().split())
_map = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for i in range(n):
    _map[i] = list(map(int, sys.stdin.readline().rstrip().split()))

prev_li_c = [[0, 0]]
cnt = 0
while True:
    li_c = []
    for y, x in prev_li_c:
        dfs(_map, visited, y, x, li_c)

    for y, x in li_c:
        _map[y][x] = 0
        visited[y][x] = 0

    if len(li_c) == 0:
        break
    cnt += 1

    prev_li_c = li_c

print(cnt)
print(len(prev_li_c))
