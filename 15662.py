import sys
from collections import deque


def rotate_gear(li, n, d):
    l = li[n][6]
    r = li[n][2]

    if d == 1:
        li[n].rotate(1)
    else:
        li[n].rotate(-1)

    if n >= 1 and l != li[n - 1][2] and visited[n - 1] == 0:
        visited[n - 1] = 1
        rotate_gear(li, n - 1, -d)

    if n < t - 1 and r != li[n + 1][6] and visited[n + 1] == 0:
        visited[n + 1] = 1
        rotate_gear(li, n + 1, -d)

    return


t = int(sys.stdin.readline().rstrip())
li = []
for _ in range(t):
    q = deque(sys.stdin.readline().rstrip())
    li.append(q)

k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    n, d = map(int, sys.stdin.readline().rstrip().split())
    n -= 1

    visited = [0] * t
    visited[n] = 1
    rotate_gear(li, n, d)

cnt = 0
for i in range(t):
    if li[i][0] == "1":
        cnt += 1

print(cnt)
