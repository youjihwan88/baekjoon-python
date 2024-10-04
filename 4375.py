while True:
    try:
        n = int(input())
    except EOFError:
        break

    val = 1
    cnt = 1
    while True:
        if val % n == 0:
            break

        val *= 10
        val += 1
        val %= n
        cnt += 1

    print(cnt)
