import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

rst = 0

_map = [["" for _ in range(m)] for _ in range(n)]
visited_alp = [False] * 26
for i in range(n):
    in_data = sys.stdin.readline().rstrip()
    for j in range(m):
        _map[i][j] = in_data[j]


def dfs(y, x, cnt):
    global rst
    rst = max(cnt, rst)

    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny = y + dy
        nx = x + dx

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        idx = ord(_map[ny][nx]) - ord("A")
        if visited_alp[idx] == False:
            visited_alp[idx] = True
            dfs(ny, nx, cnt + 1)
            visited_alp[idx] = False

    return


visited_alp[ord(_map[0][0]) - ord("A")] = True
dfs(0, 0, 1)

print(rst)
