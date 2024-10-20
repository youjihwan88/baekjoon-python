while True:
    li = list(map(int, input().split()))

    if li[0] == 0:
        break

    rst = 1
    for i in range(li[0]):
        rst *= li[2 * i + 1]
        rst -= li[2 * i + 2]

    print(rst)
