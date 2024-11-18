import sys

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().rstrip().split())
li = [[] for _ in range(n)]
visited = [0] * n

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    i -= 1
    j -= 1
    li[i].append(j)
    li[j].append(i)


def dfs(here):
    for there in li[here]:
        if visited[there] == 0:
            visited[there] = 1
            dfs(there)


cnt = 0
for i in range(n):
    if visited[i] == 0:
        visited[i] = 1
        dfs(i)
        cnt += 1

print(cnt)
