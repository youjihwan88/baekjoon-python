x = int(input())
n = int(input())

sum = 0
for _ in range(n):
    sum += int(input())

print(x * (n + 1) - sum)
