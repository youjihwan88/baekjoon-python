n = int(input())

cnt = 0
num = 666
while True:
    if "666" in str(num):
        cnt += 1
    if cnt == n:
        break
    else:
        num += 1

print(num)
