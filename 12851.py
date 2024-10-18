from collections import deque


def get_nx(x, i):
    nx = 0
    if i == 0:
        nx = x - 1
    elif i == 1:
        nx = x + 1
    elif i == 2:
        nx = x * 2

    if nx >= 0 and nx < 200001:
        return nx
    else:
        return -1


n, k = map(int, input().split())

q = deque()
visited = [0] * 200001
cnt = [0] * 200001

q.append(n)
visited[n] = 1
cnt[n] = 1

time_cnt = 0
b_sucess = False
while True:
    size = len(q)
    for _ in range(size):
        x = q.popleft()

        if x == k:
            b_sucess = True

        for i in range(3):
            nx = get_nx(x, i)
            if nx == -1:
                continue

            if visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[x] + 1
                cnt[nx] += cnt[x]
            elif visited[nx] == visited[x] + 1:
                cnt[nx] += cnt[x]

    if b_sucess:
        break

    time_cnt += 1

print(visited[k] - 1)
print(cnt[k])
