li = [0] * 1000001
li[0] = -1
li[1] = -1
for i in range(2, len(li)):
    if li[i] == 0:
        li[i] = 1
    else:
        continue
    j = 2
    while True:
        if i * j >= len(li):
            break

        li[i * j] = -1
        j += 1

m, n = map(int, input().split())

for i in range(m, n + 1):
    if li[i] == 1:
        print(i)
