n = int(input())

for i in range(n):
    s = "*" * (i + 1) + " " * 2 * (n - i - 1) + "*" * (i + 1)
    print(s)

for i in range(n - 2, -1, -1):
    s = "*" * (i + 1) + " " * 2 * (n - i - 1) + "*" * (i + 1)
    print(s)
