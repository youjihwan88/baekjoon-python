import sys

t = int(sys.stdin.readline().rstrip())

for j in range(t):
    n = int(sys.stdin.readline().rstrip())

    while True:
        b_success = True
        str_n = str(n)
        for i in range(len(str_n) - 1):
            if int(str_n[i]) <= int(str_n[i + 1]):
                continue
            else:
                b_success = False
                break

        if b_success:
            break

        n -= 1

    print(f"Case #{j+1}: {n}")
