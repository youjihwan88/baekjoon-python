import sys

n = int(sys.stdin.readline().rstrip())
d = {}
for _ in range(n):
    d[sys.stdin.readline().rstrip()] = 1

m = int(sys.stdin.readline().rstrip())
cnt = 0
rst = 0
for i in range(m):
    word = sys.stdin.readline().rstrip()
    if d.get(word) is not None and d.get(word) == 1:
        d[word] += 1
        cnt += 1

    if rst == 0 and cnt >= (n // 2 + (1 if n % 2 else 0)):
        rst = i + 1

print(rst)
