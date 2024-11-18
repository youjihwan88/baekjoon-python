import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

dict = {}
for _ in range(n):
    key, val = sys.stdin.readline().rstrip().split()
    dict[key] = val

for _ in range(m):
    key = sys.stdin.readline().rstrip()
    print(dict[key])
