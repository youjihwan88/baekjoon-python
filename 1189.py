import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
li = [["" for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    in_data = sys.stdin.readline().rstrip()
    for j in range(m):
        li[i][j] = in_data[j]

rst = 0


def dfs(y, x, cnt):
    global rst
    if y == 0 and x == m - 1:
        if cnt == k:
            rst += 1
        return

    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny = y + dy
        nx = x + dx

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        if li[ny][nx] == "." and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            dfs(ny, nx, cnt + 1)
            visited[ny][nx] = 0
    return


if li[n - 1][0] == "T":
    print(0)
else:
    visited[n - 1][0] = 1
    dfs(n - 1, 0, 1)
    print(rst)
