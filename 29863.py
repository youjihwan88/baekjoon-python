s = int(input())
e = int(input())

rst = e - s
if rst < 0:
    rst += 24

print(rst)
