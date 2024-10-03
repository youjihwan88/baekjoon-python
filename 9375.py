t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0:
        print(0)
        continue

    dict = {}
    for _ in range(n):
        data = input().split()
        if dict.get(data[1]) is None:
            dict[data[1]] = []
        dict[data[1]].append(data[0])

    rst = 1
    for k, v in dict.items():
        rst *= len(v) + 1
    rst -= 1
    print(rst)
