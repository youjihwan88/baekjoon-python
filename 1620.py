import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li = [""] * n
dict = {}

for i in range(n):
    data = sys.stdin.readline().rstrip()
    li[i] = data
    dict[data] = i

for _ in range(m):
    data = sys.stdin.readline().rstrip()

    if data.isdigit():
        print(li[int(data) - 1])
    else:
        print(dict[data] + 1)
