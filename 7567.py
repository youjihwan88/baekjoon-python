s = input()

prev_c = ""
rst = 0
for c in s:
    if c == prev_c:
        rst += 5
    else:
        rst += 10

    prev_c = c

print(rst)
