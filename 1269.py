import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
s1 = set(map(int, sys.stdin.readline().rstrip().split()))
s2 = set(map(int, sys.stdin.readline().rstrip().split()))

print(len(s1) + len(s2) - 2 * len(s1.intersection(s2)))
