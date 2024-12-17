import sys

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))
d = [1] * n
prev_idx = [-1] * n
rst_val = 0
rst_idx = 0

for i in range(n):
    for j in range(i):
        if li[i] > li[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            prev_idx[i] = j

    if d[i] > rst_val:
        rst_val = d[i]
        rst_idx = i

i = rst_idx
rst_li = []
while i != -1:
    rst_li.append(li[i])
    i = prev_idx[i]

print(len(rst_li))
print(*rst_li[::-1], sep=" ")
