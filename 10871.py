import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

for i in data:
    if i < x:
        print(i, end=" ")
