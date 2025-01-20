import sys
from copy import deepcopy

n1, n2 = map(int, sys.stdin.readline().rstrip().split())

li1 = sys.stdin.readline().rstrip()
li2 = sys.stdin.readline().rstrip()

t = int(sys.stdin.readline().rstrip())

li = []
for e in reversed(li1):
    li.append([e, 1])
for e in li2:
    li.append([e, -1])


for _ in range(t):
    n_li = deepcopy(li)
    for i in range(len(li) - 1):
        if li[i][1] == 1 and li[i + 1][1] == -1:
            n_li[i], n_li[i + 1] = li[i + 1], li[i]

    li = deepcopy(n_li)

for e in li:
    print(e[0], end="")
