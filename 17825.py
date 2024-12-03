from itertools import product

# [score, next_idx]
_map = [
    [0, [1, 2, 3, 4, 5]],
    [2, [2, 3, 4, 5, 6]],
    [4, [3, 4, 5, 6, 7]],
    [6, [4, 5, 6, 7, 8]],
    [8, [5, 6, 7, 8, 9]],
    [10, [20, 21, 22, 28, 29]],
    [12, [7, 8, 9, 10, 11]],
    [14, [8, 9, 10, 11, 12]],
    [16, [9, 10, 11, 12, 13]],
    [18, [10, 11, 12, 13, 14]],
    [20, [23, 24, 28, 29, 30]],
    [22, [12, 13, 14, 15, 16]],
    [24, [13, 14, 15, 16, 17]],
    [26, [14, 15, 16, 17, 18]],
    [28, [15, 16, 17, 18, 19]],
    [30, [25, 26, 27, 28, 29]],
    [32, [17, 18, 19, 31, 32]],
    [34, [18, 19, 31, 32, 32]],
    [36, [19, 31, 32, 32, 32]],
    [38, [31, 32, 32, 32, 32]],
    [13, [21, 22, 28, 29, 30]],
    [16, [22, 28, 29, 30, 31]],
    [19, [28, 29, 30, 31, 32]],
    [22, [24, 28, 29, 30, 31]],
    [24, [28, 29, 30, 31, 32]],
    [28, [26, 27, 28, 29, 30]],
    [27, [27, 28, 29, 30, 31]],
    [26, [28, 29, 30, 31, 32]],
    [25, [29, 30, 31, 32, 32]],
    [30, [30, 31, 32, 32, 32]],
    [35, [31, 32, 32, 32, 32]],
    [40, [32, 32, 32, 32, 32]],
    [0, [32, 32, 32, 32, 32]],
]


li = list(map(int, input().split()))
_max_score = 0
for _samples in product(range(4), repeat=10):
    _loc = [0, 0, 0, 0]
    score = 0

    for i in range(10):
        curr = _loc[_samples[i]]
        if curr == 32:
            break

        next = _map[curr][1][li[i] - 1]

        if next != 32 and next in _loc:
            break

        _loc[_samples[i]] = next
        score += _map[next][0]

    _max_score = max(_max_score, score)

print(_max_score)
