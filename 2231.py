n = int(input())

rst = 0
for i in range(1, n + 1):
    sum = val = i
    while True:
        sum += val % 10
        if val // 10 == 0:
            break
        else:
            val //= 10

    if sum == n:
        rst = i
        break

print(rst)
