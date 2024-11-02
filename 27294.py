import sys

t, s = map(int, sys.stdin.readline().rstrip().split())

if s == 1 or t <= 11 or t >= 17:
    print(280)
else:
    print(320)
