import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    s = sys.stdin.readline().rstrip().split()
    print(*s[2:], sep=" ", end=" ")
    print(*s[:2], sep=" ")
