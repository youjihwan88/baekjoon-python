import sys
from copy import deepcopy

r, c, m = map(int, sys.stdin.readline().rstrip().split())
li = [[[False, 0, 0, 0] for _ in range(c)] for _ in range(r)]  # Existence, s(speed), d(direction), z(size)

for _ in range(m):
    _r, _c, _s, _d, _z = map(int, sys.stdin.readline().rstrip().split())
    li[_r - 1][_c - 1] = [True, _s, _d, _z]

my_loc = 0

rst = 0
while my_loc < c:
    # 상어 잡기
    for i in range(r):
        if li[i][my_loc][0] == True:
            rst += li[i][my_loc][3]
            li[i][my_loc] = [False, 0, 0, 0]
            break

    # 상어 이동
    new_li = [[[False, 0, 0, 0] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if li[i][j][0] == True:
                new_y = i
                new_x = j
                new_dir = li[i][j][2]

                if li[i][j][2] == 1:  # 위쪽 이동
                    new_y -= li[i][j][1] % (2 * (r - 1))
                elif li[i][j][2] == 2:  # 아래쪽 이동
                    new_y += li[i][j][1] % (2 * (r - 1))
                elif li[i][j][2] == 3:  # 오른쪽 이동
                    new_x += li[i][j][1] % (2 * (c - 1))
                elif li[i][j][2] == 4:  # 왼쪽 이동
                    new_x -= li[i][j][1] % (2 * (c - 1))

                while True:
                    if 0 <= new_y < r:
                        break
                    elif new_y < 0:
                        new_dir = 2
                        new_y = -new_y
                    elif new_y >= r:
                        new_dir = 1
                        new_y = 2 * r - new_y - 2

                while True:
                    if 0 <= new_x < c:
                        break
                    elif new_x < 0:
                        new_dir = 3
                        new_x = -new_x
                    elif new_x >= c:
                        new_dir = 4
                        new_x = 2 * c - new_x - 2

                if new_li[new_y][new_x][0] == True:
                    if li[i][j][3] > new_li[new_y][new_x][3]:
                        new_li[new_y][new_x] = [True, li[i][j][1], new_dir, li[i][j][3]]
                else:
                    new_li[new_y][new_x] = [True, li[i][j][1], new_dir, li[i][j][3]]

    # 오른쪽으로 이동
    li = new_li
    my_loc += 1

print(rst)
