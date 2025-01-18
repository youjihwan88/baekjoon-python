li = list(map(int, input().split()))

i = 1
b_break = False
while True:
    cnt = 0
    for e in li:
        if i % e == 0:
            cnt += 1

        if cnt >= 3:
            b_break = True
            break

    if b_break:
        break

    i += 1

print(i)
