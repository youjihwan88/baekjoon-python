_max = -1
_max_idx = [1, 1]
for i in range(9):
    _input = list(map(int, input().split()))

    for j in range(9):
        if _input[j] > _max:
            _max = _input[j]
            _max_idx = [i + 1, j + 1]


print(_max)
print(*_max_idx, sep=" ")
