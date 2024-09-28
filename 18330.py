n = int(input())
k = int(input())

rst = 0
if n > k + 60:
    rst = (n - k - 60) * 3000 + (k + 60) * 1500
else:
    rst = n * 1500

print(rst)
