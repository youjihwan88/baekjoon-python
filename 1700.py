import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
li = list(map(int, sys.stdin.readline().rstrip().split()))

plug = []
cnt = 0
for i in range(k):
    if li[i] in plug:
        continue

    if len(plug) < n:
        plug.append(li[i])
        continue

    loc = []
    for device in plug:
        if device in li[i:]:
            loc.append(li[i:].index(device))
        else:
            loc.append(k + 1)

    target = loc.index(max(loc))
    plug.remove(plug[target])
    plug.append(li[i])
    cnt += 1

print(cnt)
