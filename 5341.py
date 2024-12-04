import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    print(n * (n + 1) // 2)
