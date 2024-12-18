import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    while n >= 10:
        sum = 0
        for c in str(n):
            sum += int(c)
        n = sum

    print(n)
