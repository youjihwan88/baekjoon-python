import sys
import math

lines = sys.stdin.readlines()

for _input in lines:
    a, b = map(int, _input.split())

    rst = a / b
    print(f"{math.floor(rst * 100 + 0.5) / 100:.2f}")
