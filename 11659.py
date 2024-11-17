import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
li = list(map(int, sys.stdin.readline().rstrip().split()))
prefix_sum = [0]
for i in range(n):
    prefix_sum.append(prefix_sum[-1] + li[i])

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[b] - prefix_sum[a - 1])
