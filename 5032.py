e, f, c = map(int, input().split())

_sum = e + f
rst = 0
while True:
    if _sum < c:
        break

    rst += _sum // c
    _sum = _sum // c + _sum % c


print(rst)
