l = int(input())
s = input()

rst = 0
for i in range(len(s)):
    rst += (ord(s[i]) - ord("a") + 1) * pow(31, i, 1234567891)

print(rst % 1234567891)
