n = int(input())

li = list(map(int, input().split()))

for e in li:
    for i in range(256):
        if i ^ (i << 1) & 255 == e:
            print(i, end=" ")
            break
