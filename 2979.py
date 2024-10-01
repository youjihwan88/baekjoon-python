a, b, c = map(int, input().split())

li = [0] * 101
for _ in range(3):
    in_time, out_time = map(int, input().split())
    for i in range(in_time, out_time):
        li[i] += 1

sum = 0
for i in range(101):
    if li[i] == 3:
        sum += 3 * c
    elif li[i] == 2:
        sum += 2 * b
    elif li[i] == 1:
        sum += a

print(sum)
