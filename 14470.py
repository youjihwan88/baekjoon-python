a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

rst = 0
if a <= 0:
    rst += d
    if a < 0:
        rst += (-a) * c
    rst += b * e
else:
    rst += (b - a) * e

print(rst)
