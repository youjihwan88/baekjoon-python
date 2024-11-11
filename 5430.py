import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    try:
        q = deque(map(int, sys.stdin.readline().rstrip()[1:-1].split(",")))
    except:
        q = deque()

    b_fail = False
    dir = 0
    for c in p:
        if c == "R":
            dir ^= 1
        elif c == "D":
            if len(q) == 0:
                b_fail = True
                break
            if dir == 0:
                q.popleft()
            else:
                q.pop()

    if b_fail:
        print("error")
        continue
    if dir == 1:
        q.reverse()

    print("[", end="")
    print(*q, sep=",", end="")
    print("]")
