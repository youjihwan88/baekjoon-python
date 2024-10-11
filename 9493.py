import sys
import math

while True:
    m, a, b = map(int, sys.stdin.readline().rstrip().split())
    if m == 0 and a == 0 and b == 0:
        break

    a_t = m * 3600 / a
    b_t = m * 3600 / b

    diff_t = math.floor(abs(a_t - b_t) + 0.5)

    print(f"{diff_t // 3600}:{(diff_t % 3600) // 60:02d}:{diff_t % 60:02d}")
