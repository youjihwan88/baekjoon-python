a = int(input())
b = int(input())
c = int(input())

rst = a * b * c
li = [0] * 10
for c in str(rst):
    li[int(c)] += 1

print(*li, sep="\n")
