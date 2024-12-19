import math

x, y = map(int, input().split())

z = int(y * 100 / x)

if z >= 99:
    print("-1")
else:
    print(math.ceil((100 * y - (z + 1) * x) / (z - 99)))
