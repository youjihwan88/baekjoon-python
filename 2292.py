n = int(input())

i = 1
while True:
    if n <= 3 * i * i - 3 * i + 1:
        break

    i += 1

print(i)
