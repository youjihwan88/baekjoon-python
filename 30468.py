a, b, c, d, e = map(int, input().split())

sum = a + b + c + d

if sum >= e * 4:
    print("0")
else:
    print(e * 4 - sum)
