import sys

m, n = map(int, sys.stdin.readline().rstrip().split())
li = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
rst = [[[0, 0] for _ in range(m)] for _ in range(n)]
vec = []

for i in range(n):
    _input = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(m):
        li[i][j] = _input[j]


def dfs(y, x):
    for dy, dx, c in [(0, 1, 4), (1, 0, 8), (0, -1, 1), (-1, 0, 2)]:

        if li[y][x] & c:
            continue

        ny = y + dy
        nx = x + dx

        if visited[ny][nx]:
            continue

        vec.append((ny, nx))
        visited[ny][nx] = 1
        dfs(ny, nx)

    return


cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            vec.append((i, j))
            visited[i][j] = 1
            dfs(i, j)

            for y, x in vec:
                rst[y][x][0] = cnt
                rst[y][x][1] = len(vec)

            vec.clear()
            cnt += 1

max_room = 0
for i in range(n):
    for j in range(m):
        max_room = max(rst[i][j][1], max_room)

max_conn_room = 0
for i in range(n):
    for j in range(m - 1):
        if rst[i][j][0] != rst[i][j + 1][0]:
            max_conn_room = max(max_conn_room, rst[i][j][1] + rst[i][j + 1][1])
for j in range(m):
    for i in range(n - 1):
        if rst[i][j][0] != rst[i + 1][j][0]:
            max_conn_room = max(max_conn_room, rst[i][j][1] + rst[i + 1][j][1])


print(cnt)
print(max_room)
print(max_conn_room)
