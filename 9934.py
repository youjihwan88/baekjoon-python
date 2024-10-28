import sys

k = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))

rst = [[] for _ in range(k)]


def search(s, e, level):
    m = (s + e) // 2
    if e - s <= 1:
        return
    rst[level].append(li[m - 1])

    search(s, m, level + 1)
    search(m, e, level + 1)
    return


search(0, 2**k, 0)

for i in range(k):
    print(*rst[i], sep=" ")
