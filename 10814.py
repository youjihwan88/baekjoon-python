import sys

n = int(sys.stdin.readline().rstrip())
li = [[0, "", 0] for _ in range(n)]

for i in range(n):
    line = sys.stdin.readline().rstrip().split()
    li[i][0] = int(line[0])
    li[i][1] = line[1]
    li[i][2] = i

li.sort(key=lambda x: (x[0], x[2]))

for e in li:
    print(f"{e[0]} {e[1]}")
