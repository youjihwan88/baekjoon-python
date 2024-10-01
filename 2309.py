from itertools import combinations

li = []
for _ in range(9):
    li.append(int(input()))

rst = None
for val in combinations(li, 7):
    if sum(val) == 100:
        rst = list(val)
        break

rst.sort()
print(*rst, sep="\n")
