import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

q = deque()
q.appendleft((None, -1))

max_cnt = 0
for i, c in enumerate(s):
    if c == "(":
        q.append(("(", i))
    elif c == ")":
        if len(q) and q[-1][0] == "(":
            q.pop()
            max_cnt = max(max_cnt, i - q[-1][1])
        else:
            q.append((")", i))

print(max_cnt)
