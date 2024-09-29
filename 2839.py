n = int(input())

cnt_3 = 0
cnt_5 = n // 5

while True:
    if cnt_5 < 0:
        break

    if cnt_5 * 5 + cnt_3 * 3 > n:
        cnt_5 -= 1
    elif cnt_5 * 5 + cnt_3 * 3 < n:
        cnt_3 += 1
    else:
        break

if cnt_5 < 0:
    print(-1)
else:
    print(cnt_3 + cnt_5)
