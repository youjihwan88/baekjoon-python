t = int(input())

for _ in range(t):
    x = input()
    if x[0] == x[1] == x[2] == x[3]:
        continue

    cnt = 0
    while True:
        if x == "6174":
            break
        nx = str(int("".join(sorted(x, reverse=True))) - int("".join(sorted(x))))
        if len(nx) < 4:
            nx = "0" * (4 - len(nx)) + nx
        x = nx
        cnt += 1

    print(cnt)
