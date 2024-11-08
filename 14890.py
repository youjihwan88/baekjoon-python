import sys

n, l = map(int, sys.stdin.readline().rstrip().split())
li = [[0] * n for _ in range(n)]

for i in range(n):
    _input = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        li[i][j] = _input[j]

cnt = 0
# 열 탐색
for i in range(n):
    visited = [0] * n
    prev = li[i][0]

    b_fail = False
    for j in range(1, n):
        curr = li[i][j]

        if abs(curr - prev) > 1:
            b_fail = True
            break
        elif curr - prev == 1:
            for k in range(l):
                if j - 1 - k < 0:
                    b_fail = True
                    break
                if visited[j - 1 - k] == 1 or li[i][j - 1 - k] != prev:
                    b_fail = True
                    break
                visited[j - 1 - k] = 1
        elif curr - prev == -1:
            for k in range(l):
                if j + k >= n:
                    b_fail = True
                    break
                if visited[j + k] == 1 or li[i][j + k] != curr:
                    b_fail = True
                    break
                visited[j + k] = 1

        if b_fail:
            break

        prev = curr

    if not b_fail:
        cnt += 1

# 행 탐색
for j in range(n):
    visited = [0] * n
    prev = li[0][j]

    b_fail = False
    for i in range(1, n):
        curr = li[i][j]

        if abs(curr - prev) > 1:
            b_fail = True
            break
        elif curr - prev == 1:
            for k in range(l):
                if i - 1 - k < 0:
                    b_fail = True
                    break
                if visited[i - 1 - k] == 1 or li[i - 1 - k][j] != prev:
                    b_fail = True
                    break
                visited[i - 1 - k] = 1
        elif curr - prev == -1:
            for k in range(l):
                if i + k >= n:
                    b_fail = True
                    break
                if visited[i + k] == 1 or li[i + k][j] != curr:
                    b_fail = True
                    break
                visited[i + k] = 1

        if b_fail:
            break

        prev = curr

    if not b_fail:
        cnt += 1

pass
print(cnt)
