n = int(input())

_max = -1000000
_min = 1000000

vals = map(int, input().split())

for val in vals:
    if val > _max:
        _max = val

    if val < _min:
        _min = val

print(_min)
print(_max)
