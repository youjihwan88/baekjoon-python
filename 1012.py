import sys

sys.setrecursionlimit(10**6)


def dfs(_map, visited, y, x):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        if _map[ny][nx] == 1 and visited[ny][nx] == 0:
            dfs(_map, visited, ny, nx)

    return


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())

    _map = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        _map[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if _map[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                dfs(_map, visited, i, j)

    print(cnt)
