a = int(input())

rst = a * 0.01 + 25

rst = max(100, rst)
rst = min(2000, rst)

print(f"{rst:.2f}")
