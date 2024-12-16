a, b = map(int, input().split())

li = []
for i in range(1, 1000):
    if len(li) > 1000:
        break

    li.extend([i] * i)

sum = 0
for i in range(a - 1, b):
    sum += li[i]

print(sum)
