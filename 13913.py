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
prev_loc = [-1 for _ in range(200001)]

q.append(n)
prev_loc[n] = None

time_cnt = 0
b_sucess = False
while True:
    size = len(q)
    for _ in range(size):
        x = q.popleft()

        if x == k:
            b_sucess = True
            break

        for i in range(3):
            nx = get_nx(x, i)
            if nx == -1:
                continue

            if prev_loc[nx] == -1:
                q.append(nx)
                prev_loc[nx] = x

    if b_sucess:
        break

    time_cnt += 1

print(time_cnt)

li = []
val = k
while True:
    li.append(val)
    val = prev_loc[val]
    if val == None:
        break

print(*list(reversed(li)), sep=" ")
