import sys
from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, sys.stdin.readline().rstrip().split())
y1, x1, y2, x2 = map(int, sys.stdin.readline().rstrip().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

_map = [[""] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for i in range(n):
    in_data = sys.stdin.readline().rstrip()
    for j in range(m):
        _map[i][j] = in_data[j]

q = deque()
q.append((y1, x1))
visited[y1][x1] = True

time_cnt = 0
q_post = deque()
b_find = False

while True:
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if visited[ny][nx] == False:
                if _map[ny][nx] == "1":
                    q_post.append((ny, nx))
                    visited[ny][nx] = True
                elif _map[ny][nx] == "0":
                    q.append((ny, nx))
                    visited[ny][nx] = True
                elif _map[ny][nx] == "#":
                    b_find = True
                    visited[ny][nx] = True
                    break

        if b_find:
            break

    if b_find:
        break

    q = q_post.copy()
    q_post.clear()
    time_cnt += 1

print(time_cnt + 1)
