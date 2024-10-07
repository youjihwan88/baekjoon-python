import sys

sys.setrecursionlimit(10**6)


def get_flood_map(_map, flood_lv):
    n = len(_map)
    flood_map = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if _map[i][j] > flood_lv:
                flood_map[i][j] = 1
    return flood_map


def dfs(_map, visited, y, x):
    visited[y][x] = 1
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue

        if _map[ny][nx] == 1 and visited[ny][nx] == 0:
            dfs(_map, visited, ny, nx)

    return


n = int(sys.stdin.readline().rstrip())
_map = [[0] * n for _ in range(n)]

for i in range(n):
    _map[i] = list(map(int, sys.stdin.readline().rstrip().split()))

min_h = _map[0][0]
max_h = _map[0][0]
for i in range(n):
    for j in range(n):
        if _map[i][j] > max_h:
            max_h = _map[i][j]

        if _map[i][j] < min_h:
            min_h = _map[i][j]

max_rst = 0
for flood_lv in range(min_h - 1, max_h):
    flood_map = get_flood_map(_map, flood_lv)
    visited = [[0] * n for _ in range(n)]

    rst = 0
    for i in range(n):
        for j in range(n):
            if flood_map[i][j] == 1 and visited[i][j] == 0:
                rst += 1
                dfs(flood_map, visited, i, j)

    if rst > max_rst:
        max_rst = rst

print(max_rst)
