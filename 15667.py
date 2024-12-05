n = int(input())

rst = 0
i = 0
while True:
    val = i * i + i + 1
    if val == n:
        rst = i
        break
    i += 1

print(rst)
