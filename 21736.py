import sys

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().rstrip().split())
li = [["" for _ in range(m)] for _ in range(n)]
visited = [[0] * m for _ in range(n)]
start_idx = None
for i in range(n):
    _input = sys.stdin.readline().rstrip()
    for j in range(m):
        li[i][j] = _input[j]

        if li[i][j] == "I":
            start_idx = [i, j]


cnt = 0


def dfs(y, x):
    global cnt
    for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ny = y + dy
        nx = x + dx

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        if visited[ny][nx] == 0 and li[ny][nx] != "X":
            visited[ny][nx] = 1
            if li[ny][nx] == "P":
                cnt += 1
            dfs(ny, nx)
    return


visited[start_idx[0]][start_idx[1]] = 1
dfs(start_idx[0], start_idx[1])

if cnt == 0:
    print("TT")
else:
    print(cnt)
