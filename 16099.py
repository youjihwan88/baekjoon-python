import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    lt, wt, le, we = map(int, sys.stdin.readline().rstrip().split())

    if lt * wt > le * we:
        print("TelecomParisTech")
    elif lt * wt < le * we:
        print("Eurecom")
    else:
        print("Tie")
