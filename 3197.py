import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
_map = [["" for _ in range(m)] for _ in range(n)]
visited_water = [[False for _ in range(m)] for _ in range(n)]
visited_swan = [[-1 for _ in range(m)] for _ in range(n)]


q_swan = deque()
q_water = deque()
for i in range(n):
    _input = sys.stdin.readline().rstrip()
    for j in range(m):
        _map[i][j] = _input[j]
        if _map[i][j] == "L":
            q_swan.append((i, j))
            q_water.append((i, j))
            visited_water[i][j] = True
        elif _map[i][j] == ".":
            q_water.append((i, j))
            visited_water[i][j] = True
q_swan.pop()
visited_swan[q_swan[0][0]][q_swan[0][1]] = 0

b_sucess = False
rst = None
while True:
    q_swan_post = deque()
    while q_swan:
        y, x = q_swan.popleft()
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny = y + dy
            nx = x + dx

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if visited_swan[ny][nx] == -1:
                if _map[ny][nx] == ".":
                    q_swan.append((ny, nx))
                    visited_swan[ny][nx] = visited_swan[y][x]
                elif _map[ny][nx] == "X":
                    q_swan_post.append((ny, nx))
                    visited_swan[ny][nx] = visited_swan[y][x] + 1
                elif _map[ny][nx] == "L":
                    visited_swan[ny][nx] = visited_swan[y][x]
                    b_sucess = True
                    rst = visited_swan[ny][nx]
                    break
        if b_sucess:
            break
    if b_sucess:
        break
    q_swan = q_swan_post.copy()

    q_water_post = deque()
    while q_water:
        y, x = q_water.popleft()

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny = y + dy
            nx = x + dx

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if visited_water[ny][nx] == False:
                if _map[ny][nx] == ".":
                    q_water.append((ny, nx))
                    visited_water[ny][nx] = True
                elif _map[ny][nx] == "X":
                    q_water_post.append((ny, nx))
                    visited_water[ny][nx] = True
                    _map[ny][nx] = "."
    q_water = q_water_post.copy()

print(rst)
