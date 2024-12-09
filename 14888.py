from itertools import permutations


n = int(input())
num_li = list(map(int, input().split()))
oper = list(map(int, input().split()))
oper_li = []
for i in range(4):
    for j in range(oper[i]):
        oper_li.append(i)

max_rst = -1000000000
min_rst = 1000000000
for oper_arr in permutations(oper_li, n - 1):
    rst = num_li[0]
    for i, oper in enumerate(oper_arr):
        if oper == 0:
            rst += num_li[i + 1]
        elif oper == 1:
            rst -= num_li[i + 1]
        elif oper == 2:
            rst *= num_li[i + 1]
        elif oper == 3:
            if rst < 0:
                rst = -((-rst) // num_li[i + 1])
            else:
                rst //= num_li[i + 1]

    if rst > max_rst:
        max_rst = rst

    if rst < min_rst:
        min_rst = rst

print(max_rst)
print(min_rst)
