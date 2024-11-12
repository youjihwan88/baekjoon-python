import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque()

cnt = 0
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())

    s_cnt = 1
    while len(q) and x >= q[-1][0]:
        cnt += q[-1][1]

        if x == q[-1][0]:
            s_cnt = q[-1][1] + 1
        else:
            s_cnt = 1

        q.pop()

    if len(q):
        cnt += 1

    q.append((x, s_cnt))

print(cnt)
