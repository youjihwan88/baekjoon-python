import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li = [[0] * m for _ in range(n)]
for i in range(n):
    _input = sys.stdin.readline().rstrip()
    for j in range(m):
        li[i][j] = int(_input[j])

max_rst = 0


def search(start, visited, step, direction, rst):
    global max_rst
    if visited == (1 << n * m) - 1:
        max_rst = max(rst, max_rst)
        return

    y = start // m
    x = start % m

    val = 0
    if step == 1:
        if visited & (1 << (y * m + x)):
            return
        visited = visited | (1 << (y * m + x))
        val = li[y][x]
    elif direction == 0:
        for i in range(step):
            if visited & (1 << (y * m + (x + i))):
                return
            visited = visited | (1 << (y * m + (x + i)))
            val *= 10
            val += li[y][x + i]
    elif direction == 1:
        for i in range(step):
            if visited & (1 << ((y + i) * m + x)):
                return
            visited = visited | (1 << ((y + i) * m + x))
            val *= 10
            val += li[y + i][x]

    rst += val

    next = start + 1
    while True:
        if visited & (1 << next):
            next += 1
        else:
            break

    ny = next // m
    nx = next % m
    for i in range(m - nx):
        search(next, visited, i + 1, 0, rst)
    for i in range(1, n - ny):
        search(next, visited, i + 1, 1, rst)

    return


for i in range(m):
    search(0, 0, i + 1, 0, 0)
for i in range(1, n):
    search(0, 0, i + 1, 1, 0)

print(max_rst)
