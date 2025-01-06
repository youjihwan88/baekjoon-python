import sys

n = int(sys.stdin.readline().rstrip())
li_a = list(map(int, sys.stdin.readline().rstrip().split()))
li_b = list(map(int, sys.stdin.readline().rstrip().split()))
li_k = list(map(float, sys.stdin.readline().rstrip().split()))

rst = 0
for i in range(n):
    if li_k[i] >= 1.0:
        rst += int(li_a[i] * (li_k[i] * 10) / 10)
        rst -= li_b[i]
    else:
        rst -= int(li_b[i] * (li_k[i] * 10) / 10)
        rst += li_a[i]

print(rst)
