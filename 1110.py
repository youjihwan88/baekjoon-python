n = int(input())

val = n
cycle = 0
while True:
    r = ((val % 10) + (val // 10)) % 10
    l = val % 10

    val = l * 10 + r

    cycle += 1
    if val == n:
        break


print(cycle)
