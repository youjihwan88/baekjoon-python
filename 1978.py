n = int(input())

li = [0] * 1001
for i in range(2, len(li)):
    if li[i] == 0:
        li[i] = 1
        j = 2
        while True:
            if i * j >= len(li):
                break
            li[i * j] = -1
            j += 1

data = map(int, input().split())

rst = 0
for e in data:
    if li[e] == 1:
        rst += 1

print(rst)
