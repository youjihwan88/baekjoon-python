n = int(input())
li = list(map(int, input().split()))
li.sort()
cu_sum = [li[0]]
for i in range(1, n):
    cu_sum.append(cu_sum[-1] + li[i])

print(sum(cu_sum))
