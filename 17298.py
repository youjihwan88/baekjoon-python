import sys

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))

stk = []
rst = [-1] * n
for i in range(len(li)):
    while True:
        if len(stk) and stk[-1][1] < li[i]:
            idx, _ = stk.pop()
            rst[idx] = li[i]
        else:
            break

    stk.append((i, li[i]))

print(*rst, sep=" ")
