n, m = map(int, input().split())

rst = 0
if n <= m:
    rst = 2 * (n - 1)
else:
    rst = 2 * (m - 1) + 1

print(rst)
