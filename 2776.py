import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    st = set(map(int, sys.stdin.readline().rstrip().split()))

    m = int(sys.stdin.readline().rstrip())
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    for e in li:
        if e in st:
            print("1")
        else:
            print("0")
