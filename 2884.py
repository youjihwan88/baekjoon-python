h, m = map(int, input().split())

t = h * 60 + m - 45
if t < 0:
    t += 60 * 24

print(f"{t // 60} {t % 60}")
