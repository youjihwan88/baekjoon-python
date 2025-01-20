import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    c, r, x, y = map(int, sys.stdin.readline().rstrip().split())

    cnt = 0
    visited = [[False] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if visited[i][j] == False:
                visited[i][j] = True
                cnt += 1

                if i + y < r and j + x < c:
                    visited[i + y][j + x] = True

    print(cnt)
