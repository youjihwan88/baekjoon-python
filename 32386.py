import sys

n = int(sys.stdin.readline().rstrip())
dict = {}
for _ in range(n):
    li = sys.stdin.readline().rstrip().split()
    for e in li[2:]:
        if dict.get(e) is None:
            dict[e] = 1
        else:
            dict[e] += 1

max_idx = "-1"
max_val = 0
for k, v in dict.items():
    if dict[k] > max_val:
        max_val = dict[k]
        max_idx = k
    elif dict[k] == max_val:
        max_idx = "-1"

print(max_idx)
