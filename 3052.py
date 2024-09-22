li = [0] * 42

for _ in range(10):
    a = int(input())
    li[a % 42] = 1

print(sum(li))
