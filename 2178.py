from collections import deque

n, m = map(int, input().split())
map = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    in_data = input()
    for j in range(m):
        map[i][j] = int(in_data[j])

q = deque()
visited[0][0] = 1
q.append((0, 0))

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
while len(q):
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        if map[ny][nx] == 1 and visited[ny][nx] == 0:
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))

print(visited[n - 1][m - 1])
