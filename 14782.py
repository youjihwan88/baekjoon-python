import math

n = int(input())

i = 1
sum = 0
while True:
    if i > math.sqrt(n):
        break

    if n % i == 0:
        if i == n // i:
            sum += i
        else:
            sum += i
            sum += n // i

    i += 1

print(sum)
