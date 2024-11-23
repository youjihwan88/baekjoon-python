n = int(input())

for i in range(n):
    s = " " * (n - i - 1) + "*" * (2 * i + 1)
    print(s)

for i in range(n - 1):
    s = " " * (i + 1) + "*" * (2 * (n - i - 2) + 1)
    print(s)
