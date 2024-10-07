import sys

sys.setrecursionlimit(10**6)


def dfs(_map, visited, y, x):
    visited[y][x] = 1
    cnt = 1

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue

        if _map[ny][nx] == 1 and visited[ny][nx] == 0:
            cnt += dfs(_map, visited, ny, nx)

    return cnt


n, m, k = map(int, sys.stdin.readline().rstrip().split())
_map = [[1] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            _map[i][j] = 0

conn_comp_li = []
for i in range(n):
    for j in range(m):
        if _map[i][j] == 1 and visited[i][j] == 0:
            conn_comp_li.append(dfs(_map, visited, i, j))

print(len(conn_comp_li))
print(*sorted(conn_comp_li), sep=" ")
