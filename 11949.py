import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().rstrip()))

for i in range(1, m + 1):
    for j in range(n - 1):
        if li[j] % i > li[j + 1] % i:
            tmp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = tmp

print(*li, sep="\n")
