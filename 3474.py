import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    v = 5
    cnt = 0
    while True:
        if v > n:
            break
        cnt += n // v
        v *= 5

    print(cnt)
