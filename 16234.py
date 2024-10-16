import sys
from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(_map, visited, y, x):
    visited[y][x] = True
    q = deque()
    q.append((y, x))

    conn_comp = []
    while q:
        y, x = q.popleft()
        conn_comp.append((y, x))
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue

            if l <= abs(_map[ny][nx] - _map[y][x]) <= r and visited[ny][nx] == False:
                visited[ny][nx] = True
                q.append((ny, nx))

    return conn_comp


n, l, r = map(int, sys.stdin.readline().rstrip().split())
_map = [[0] * n for _ in range(n)]

for i in range(n):
    _map[i] = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
while True:
    # 인접한 국경 탐색
    visited = [[False] * n for _ in range(n)]
    conn_comp_li = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                conn_comp_li.append(bfs(_map, visited, i, j))

    # 인접한 국경이 없으면 종료
    if len(conn_comp_li) == n * n:
        break

    # 인구이동
    for conn_comp in conn_comp_li:
        if len(conn_comp) == 1:
            continue

        sum = 0
        for y, x in conn_comp:
            sum += _map[y][x]

        for y, x in conn_comp:
            _map[y][x] = int(sum / len(conn_comp))

    cnt += 1

print(cnt)
