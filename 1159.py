import sys

n = int(sys.stdin.readline().rstrip())

cnt = [0] * 26
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    cnt[ord(name[0]) - ord("a")] += 1

b_fail = True
for i in range(len(cnt)):
    if cnt[i] >= 5:
        print(chr(i + 97), end="")
        b_fail = False

if b_fail:
    print("PREDAJA")
