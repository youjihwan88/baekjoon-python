import sys
import math

n = int(sys.stdin.readline().rstrip())
if n == 0:
    print(0)
    sys.exit()

ignored_n = math.floor(n * 0.15 + 0.5)
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().rstrip()))

li.sort()

rst = math.floor(sum(li[ignored_n : n - ignored_n]) / (n - 2 * ignored_n) + 0.5)
print(rst)
