import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
eq = sys.stdin.readline().rstrip()

num_li = [int(eq[i]) for i in range(0, len(eq), 2)]
op_li = [eq[i] for i in range(1, len(eq), 2)]

rst = -pow(2, 31)


def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b


def search(idx, val):
    global rst
    if idx == len(num_li) - 1:
        rst = max(rst, val)
        return

    search(idx + 1, calc(val, num_li[idx + 1], op_li[idx]))

    if idx < len(num_li) - 2:
        temp = calc(num_li[idx + 1], num_li[idx + 2], op_li[idx + 1])
        search(idx + 2, calc(val, temp, op_li[idx]))

    return


search(0, num_li[0])
print(rst)
