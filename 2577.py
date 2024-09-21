a = int(input())
b = int(input())
c = int(input())

rst = a * b * c
cnt = [0] * 10

for char in str(rst):
    cnt[int(char)] += 1

for i in cnt:
    print(i)
