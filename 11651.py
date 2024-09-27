import sys

n = int(sys.stdin.readline().rstrip())
li = [[0, 0] for _ in range(n)]

for i in range(len(li)):
    li[i] = list(map(int, sys.stdin.readline().rstrip().split()))

li.sort(key=lambda x: (x[1], x[0]))

for i in range(len(li)):
    print(f"{li[i][0]} {li[i][1]}")
