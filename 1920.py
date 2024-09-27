import sys

n = int(sys.stdin.readline().rstrip())
st = set(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
in_data = map(int, sys.stdin.readline().rstrip().split())
for e in in_data:
    if e in st:
        print(1)
    else:
        print(0)
