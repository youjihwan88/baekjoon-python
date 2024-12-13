import sys

n = int(sys.stdin.readline().rstrip())

cnt = -(n - 1)
for _ in range(n):
    cnt += int(sys.stdin.readline().rstrip())
print(cnt)
