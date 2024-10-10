import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
in_data = list(map(int, sys.stdin.readline().rstrip().split()))
node_to_delete = int(sys.stdin.readline().rstrip())

li = [[] for _ in range(n)]
root = 0
for i, v in enumerate(in_data):
    if v == -1:
        root = i
    elif i == node_to_delete:
        continue
    else:
        li[v].append(i)

li[node_to_delete] = None

q = deque()
q.append(root)

cnt = 0
while True:
    if len(q) == 0:
        break
    i = q.popleft()

    if li[i] == None:
        continue

    if len(li[i]) == 0:
        cnt += 1
    for node in li[i]:
        q.append(node)

print(cnt)
