while True:
    li = list(map(int, input().split()))

    if li[0] == 0:
        break

    n = li[0]
    print(li[1], end=" ")
    for i in range(2, n + 1):
        if li[i] == li[i - 1]:
            continue
        print(li[i], end=" ")
    print("$")
