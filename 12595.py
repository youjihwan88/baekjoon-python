import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    g = int(sys.stdin.readline().rstrip())
    li = list(map(int, sys.stdin.readline().rstrip().split()))

    dict = {}
    for e in li:
        if dict.get(e) is None:
            dict[e] = 1
        else:
            dict[e] += 2

    rst = None
    for k, v in dict.items():
        if v == 1:
            rst = k

    print(f"Case #{i+1}: {rst}")
