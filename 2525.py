h, m = map(int, input().split())
t = int(input())

rst = h * 60 + m + t

if rst >= 60 * 24:
    rst -= 60 * 24

print(f"{rst//60} {rst%60}")
