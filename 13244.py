import sys

t = int(sys.stdin.readline().rstrip())


def dfs(here):
    for there in li[here]:
        if visited[there] == 0:
            visited[there] = 1
            dfs(there)


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    li = [[] for _ in range(n)]
    visited = [0] * n

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        li[a - 1].append(b - 1)
        li[b - 1].append(a - 1)

    if m != n - 1:
        print("graph")
        continue

    visited[0] = 1
    dfs(0)

    if sum(visited) == n:
        print("tree")
    else:
        print("graph")
