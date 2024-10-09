import sys

h, w = map(int, sys.stdin.readline().rstrip().split())
_map = [[" "] * w for _ in range(h)]
rst = [[0] * w for _ in range(h)]

for i in range(h):
    in_data = sys.stdin.readline().rstrip()
    for j in range(w):
        _map[i][j] = in_data[j]

for i in range(h):
    cloud_x = -1
    for j in range(w):
        if _map[i][j] == "c":
            cloud_x = 0
        else:
            if cloud_x > -1:
                cloud_x += 1

        rst[i][j] = cloud_x

for i in range(h):
    print(*rst[i], sep=" ")
