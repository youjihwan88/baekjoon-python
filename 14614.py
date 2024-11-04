import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())

if c % 2 == 1:
    a = a ^ b
print(a)
