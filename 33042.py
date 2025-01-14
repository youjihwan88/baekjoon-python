import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
li = list(sys.stdin.readline().rstrip().split())

dict = defaultdict(lambda: 0)
rst = None
for i, e in enumerate(li):
    dict[e] += 1
    if dict[e] == 5:
        rst = i
        break

if rst is not None:
    print(rst + 1)
else:
    print(0)
