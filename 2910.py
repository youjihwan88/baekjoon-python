n, c = map(int, input().split())
dict = {}

for i, val in enumerate(map(int, input().split())):
    if dict.get(val) is None:
        dict[val] = [1, i]
    else:
        dict[val][0] += 1

for key, val in sorted(dict.items(), key=lambda x: (-x[1][0], x[1][1])):
    for _ in range(val[0]):
        print(key, end=" ")
