w, p, n = map(int, input().split())
li = list(map(int, input().split()))

cnt = 0
for e in li:
    if w <= e <= p:
        cnt += 1

print(cnt)
