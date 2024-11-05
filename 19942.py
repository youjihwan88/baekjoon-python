import sys

n = int(sys.stdin.readline().rstrip())
mp, mf, ms, mv = map(int, sys.stdin.readline().rstrip().split())
limit = [mp, mf, ms, mv]

li = []
min_cost = 1
rst = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().rstrip().split())))
    min_cost += li[-1][4]

b_comp_fail = True
for i in range(1 << n):
    sum = [0, 0, 0, 0, 0]
    for j in range(n):
        if (i & (1 << j)):
            for k in range(5):
                sum[k] += li[j][k]
    
    b_fail = False
    for k in range(4):
        if sum[k] < limit[k]:
            b_fail = True
            break
    
    if not b_fail:
        b_comp_fail = False
        if sum[4] < min_cost:
            min_cost = sum[4]
            rst.clear()
            for j in range(n):
                if (i & (1 << j)):
                    rst.append(j+1)
        elif sum[4] == min_cost:
            _tmp = []
            for j in range(n):
                if (i & (1 << j)):
                    _tmp.append(j+1)
            if _tmp < rst:
                rst = _tmp

if b_comp_fail:
    print("-1")
else:
    print(min_cost)
    print(*rst, sep=" ")