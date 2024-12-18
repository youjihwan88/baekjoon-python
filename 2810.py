import sys

n = int(sys.stdin.readline().rstrip())
s = input()

cnt = 1
for c in s:
    if c == "L":
        cnt -= 0.5

print(n + min(0, int(cnt)))
