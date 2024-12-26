k = int(input())

li = [1, 0]
for i in range(k):
    x, y = li[1], li[0] + li[1]

    li = [x, y]

print(*li, sep=" ")
