x, y = map(int, input().split())
min_ratio = x / y
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    ratio = x / y

    min_ratio = min(ratio, min_ratio)

print(min_ratio * 1000)
