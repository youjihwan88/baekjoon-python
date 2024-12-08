s, n = input().split()
n = int(n)

rst = 0
for c in s:
    rst *= n
    if ord("0") <= ord(c) <= ord("9"):
        rst += ord(c) - ord("0")
    else:
        rst += ord(c) - ord("A") + 10

print(rst)
