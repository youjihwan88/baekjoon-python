import sys
from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, sys.stdin.readline().rstrip().split())
_map = [[" "] * m for _ in range(n)]
visited_jihwoon = [[0] * m for _ in range(n)]
visited_fire = [[0] * m for _ in range(n)]

jihwoon_loc = []
fire_loc = []
for i in range(n):
    in_str = sys.stdin.readline().rstrip()
    for j in range(m):
        _map[i][j] = in_str[j]
        if _map[i][j] == "J":
            jihwoon_loc.append((i, j))
        elif _map[i][j] == "F":
            fire_loc.append((i, j))

q_jihwoon_prev = deque()
q_fire_prev = deque()
q_jihwoon_prev.append(jihwoon_loc[0])
visited_jihwoon[jihwoon_loc[0][0]][jihwoon_loc[0][1]] = 1
for fire in fire_loc:
    q_fire_prev.append(fire)
    visited_fire[fire[0]][fire[1]] = 1

b_success = False
cnt = 0
while True:
    q_jihwoon = deque()
    q_fire = deque()

    if len(q_jihwoon_prev) == 0:
        b_success = False
        break

    # move fire
    while q_fire_prev:
        y, x = q_fire_prev.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if _map[ny][nx] != "#" and visited_fire[ny][nx] == 0:
                visited_fire[ny][nx] = visited_fire[y][x] + 1
                _map[ny][nx] = "F"
                q_fire.append((ny, nx))

    # move jihwoon
    while q_jihwoon_prev:
        y, x = q_jihwoon_prev.popleft()
        # check if edge
        if y == 0 or x == 0 or y == n - 1 or x == m - 1:
            b_success = True
            cnt = visited_jihwoon[y][x]
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if _map[ny][nx] == "." and visited_jihwoon[ny][nx] == 0:
                visited_jihwoon[ny][nx] = visited_jihwoon[y][x] + 1
                q_jihwoon.append((ny, nx))

    if b_success:
        break

    q_jihwoon_prev = q_jihwoon
    q_fire_prev = q_fire

if b_success:
    print(cnt)
else:
    print("IMPOSSIBLE")
