from collections import deque

n = int(input())
li = list(map(int, input().split())) + [0] * (3 - n)
visited = [[[0] * 61 for _ in range(61)] for _ in range(61)]
dx = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]

q = deque()
q.append(li)
visited[li[0]][li[1]][li[2]] = 1

b_success = False
cnt = 0
while q:
    size = len(q)
    for _ in range(size):
        a, b, c = q.popleft()

        for i in range(6):
            na = max(a - dx[i][0], 0)
            nb = max(b - dx[i][1], 0)
            nc = max(c - dx[i][2], 0)

            if na <= 0 and nb <= 0 and nc <= 0:
                b_success = True
                break

            if visited[na][nb][nc] == 0:
                q.append((na, nb, nc))
                visited[na][nb][nc] = visited[a][b][c] + 1

    cnt += 1
    if b_success:
        break

print(cnt)
