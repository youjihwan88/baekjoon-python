import sys

n = int(sys.stdin.readline().rstrip())

li = []
for _ in range(n):
    in_data = sys.stdin.readline()

    num = 0
    b_is_prev_char_num = False
    for c in in_data:
        if ord(c) >= ord("0") and ord(c) <= ord("9"):
            num = num * 10 + int(c)
            b_is_prev_char_num = True
        else:
            if b_is_prev_char_num:
                li.append(num)
                num = 0
            b_is_prev_char_num = False

li.sort()
print(*li, sep="\n")
