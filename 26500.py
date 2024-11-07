import sys
import math

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(float, sys.stdin.readline().rstrip().split())
    print(f"{abs(n-m):.1f}")
