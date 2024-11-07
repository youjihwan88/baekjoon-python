import sys

lines = sys.stdin.readlines()
lines = [line.strip() for line in lines]

idx = 0
while True:
    b_break = True
    for i in range(len(lines)):
        if idx < len(lines[i]):
            b_break = False
            print(lines[i][idx], end="")

    if b_break:
        break
    idx += 1
