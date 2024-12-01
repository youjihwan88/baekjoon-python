import sys
from collections import deque


def enter_apple(e):
    return int(e) - 1


apple_loc = []
d_direction = deque()
n = int(sys.stdin.readline().rstrip())
_map = [[0] * n for _ in range(n)]

k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    apple_loc.append(list(map(enter_apple, sys.stdin.readline().rstrip().split())))
    _map[apple_loc[-1][0]][apple_loc[-1][1]] = 1

l = int(sys.stdin.readline().rstrip())
for _ in range(l):
    x, c = sys.stdin.readline().rstrip().split()
    d_direction.append([int(x), c])

cnt = 0
snake_loc = deque([[0, 0]])
direction_li = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dir_idx = 0
while True:
    # 이동 방향 결정
    if d_direction and d_direction[0][0] == cnt:
        x, c = d_direction.popleft()
        if c == "D":
            dir_idx = (dir_idx + 1) % 4
        elif c == "L":
            dir_idx = (dir_idx + 3) % 4

    # 머리 이동
    head = snake_loc[0]
    new_head = [head[0] + direction_li[dir_idx][0], head[1] + direction_li[dir_idx][1]]

    # 벽에 박으면 사망
    if new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= n or new_head[1] >= n:
        break

    # 자기자신과 부딪히면 사망
    if new_head in snake_loc:
        break

    snake_loc.appendleft(new_head)

    # 사과가 있으면 뱀의 길이 그대로, 맵에서 사과 제거
    if _map[new_head[0]][new_head[1]] == 1:
        _map[new_head[0]][new_head[1]] = 0
    # 사과가 있지 않으면 꼬리 제거
    else:
        snake_loc.pop()

    cnt += 1

print(cnt + 1)
