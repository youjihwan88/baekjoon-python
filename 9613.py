import sys
import math

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    li = list(map(int, sys.stdin.readline().rstrip().split()))

    rst = 0
    for i in range(1, len(li)):
        for j in range(i + 1, len(li)):
            rst += math.gcd(li[i], li[j])
    print(rst)
