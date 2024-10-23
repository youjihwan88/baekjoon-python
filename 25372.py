import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    data = sys.stdin.readline().rstrip()

    if len(data) >= 6 and len(data) <= 9:
        print("yes")
    else:
        print("no")
