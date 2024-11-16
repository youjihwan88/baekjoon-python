import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
visited = [0] * n

cnt = 0
for i in range(n - 3):
    if (
        s[i] == "p"
        and s[i + 1] == "P"
        and s[i + 2] == "A"
        and s[i + 3] == "p"
        and visited[i] == 0
        and visited[i + 1] == 0
        and visited[i + 2] == 0
        and visited[i + 3] == 0
    ):
        cnt += 1
        visited[i] = 1
        visited[i + 1] = 1
        visited[i + 2] = 1
        visited[i + 3] = 1

print(cnt)
