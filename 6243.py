import sys
from math import ceil

rst = 0
while True:
    _in = list(sys.stdin.readline().rstrip().split())

    if len(_in) == 1:
        if _in[0] == "0":
            print(rst)
            rst = 0
            continue
        elif _in[0] == "#":
            break

    val = int(_in[2])
    _cls = _in[3]

    if _cls == "F":
        rst += ceil(val * 2)
    elif _cls == "B":
        rst += ceil(val * 1.5)
    elif _cls == "Y":
        if val <= 500:
            rst += 500
        else:
            rst += ceil(val)
