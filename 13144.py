import sys

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))

visited = [0] * 100001

s = 0
e = 0
cnt = 0
while e < n:
    if visited[li[e]] == 0:
        visited[li[e]] = 1
        e += 1
    else:
        cnt += e - s
        visited[li[s]] = 0
        s += 1

cnt += (e - s) * (e - s + 1) // 2
print(cnt)
