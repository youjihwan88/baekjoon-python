a, b, c = map(int, input().split())
n = int(input())

_max = 0
for _ in range(n):
    score = 0
    for _ in range(3):
        x, y, z = map(int, input().split())
        score += a * x + b * y + c * z

    _max = max(score, _max)

print(_max)
