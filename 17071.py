from collections import deque

n, k = map(int, input().split())

q = deque()
visited = [[0, 0] for _ in range(500001)]
time_cnt = 0


q.append(n)
visited[n][time_cnt % 2] = 1

b_sucess = False

while True:
    size = len(q)
    for _ in range(size):
        x = q.popleft()

        if visited[k][time_cnt % 2] != 0:
            b_sucess = True
            break

        for i in range(3):
            if i == 0:
                nx = x - 1
            elif i == 1:
                nx = x + 1
            elif i == 2:
                nx = 2 * x

            if nx < 0 or nx > 500000:
                continue

            if visited[nx][(time_cnt + 1) % 2] == 0:
                q.append(nx)
                visited[nx][(time_cnt + 1) % 2] = visited[x][time_cnt % 2] + 1

    if b_sucess:
        break

    time_cnt += 1
    k += time_cnt

    if k > 500000:
        time_cnt = -1
        break

print(time_cnt)
