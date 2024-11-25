li = [1, 1, 2, 2, 2, 8]

_input = list(map(int, input().split()))
rst = []
for i in range(6):
    rst.append((li[i] - _input[i]))

print(*rst, sep=" ")
