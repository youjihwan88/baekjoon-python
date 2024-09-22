n = int(input())
li = list(map(int, input().split()))
t, p = map(int, input().split())

rst = 0
for e in li:
    rst += (e - 1) // t + 1

print(f"{rst}")
print(f"{n // p} {n % p}")
