import sys

t = int(sys.stdin.readline().rstrip())

li = [1, 1, 1, 2, 2]
for i in range(5, 101):
    li.append(li[i - 1] + li[i - 5])

for _ in range(t):
    i = int(sys.stdin.readline().rstrip())
    print(li[i - 1])
