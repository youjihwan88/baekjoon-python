def calc(a, b, c):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return (calc(a, b // 2, c) ** 2) % c

    else:
        return (((calc(a, b // 2, c) ** 2) % c) * (a % c)) % c


a, b, c = map(int, input().split())
print(calc(a, b, c))
