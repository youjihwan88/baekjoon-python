import sys

n = int(sys.stdin.readline().rstrip())
li = [0] * n

for i in range(n):
    li[i] = int(sys.stdin.readline().rstrip())

li.sort()

print(*li, sep="\n")
