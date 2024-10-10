import sys
import copy
from itertools import combinations

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dfs(_map, visited, y, x):
    visited[y][x] = 1
    _map[y][x] = 2

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue

        if _map[ny][nx] == 0 and visited[ny][nx] == 0:
            dfs(_map, visited, ny, nx)
    return


n, m = map(int, sys.stdin.readline().rstrip().split())
org_map = [[0] * m for _ in range(n)]

empty_li = []
for i in range(n):
    org_map[i] = list(map(int, sys.stdin.readline().rstrip().split()))

    for j in range(m):
        if org_map[i][j] == 0:
            empty_li.append([i, j])

max_cnt = 0
for w1, w2, w3 in combinations(empty_li, 3):
    _map = copy.deepcopy(org_map)

    visited = [[0] * m for _ in range(n)]
    _map[w1[0]][w1[1]] = 1
    _map[w2[0]][w2[1]] = 1
    _map[w3[0]][w3[1]] = 1

    for i in range(n):
        for j in range(m):
            if _map[i][j] == 2 and visited[i][j] == 0:
                dfs(_map, visited, i, j)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if _map[i][j] == 0:
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)
