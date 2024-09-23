n = int(input())
scores = list(map(int, input().split()))

sum = sum(scores)
print(sum / n * 100 / max(scores))
