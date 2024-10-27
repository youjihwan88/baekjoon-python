from itertools import permutations

k = int(input())
op_li = input().split()
num_li = list(range(10))

_min = 10 ** (k + 1)
_max = -1

for nums in permutations(num_li, k + 1):
    b_fail = False
    for i in range(k):
        if op_li[i] == "<":
            if nums[i] > nums[i + 1]:
                b_fail = True
                break
        elif op_li[i] == ">":
            if nums[i] < nums[i + 1]:
                b_fail = True
                break

    if not b_fail:
        val = int("".join(map(str, nums)))
        _min = min(_min, val)
        break


for nums in permutations(reversed(num_li), k + 1):
    b_fail = False
    for i in range(k):
        if op_li[i] == "<":
            if nums[i] > nums[i + 1]:
                b_fail = True
                break
        elif op_li[i] == ">":
            if nums[i] < nums[i + 1]:
                b_fail = True
                break

    if not b_fail:
        val = int("".join(map(str, nums)))
        _max = max(_max, val)
        break

print(f"{_max:0{k+1}d}")
print(f"{_min:0{k+1}d}")
