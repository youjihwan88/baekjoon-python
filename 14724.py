import sys

n = int(sys.stdin.readline().rstrip())

li = []
for i in range(9):
    li.append(max(list(map(int, sys.stdin.readline().rstrip().split()))))

_max = li[0]
_max_idx = 0
for i, e in enumerate(li):
    if e > _max:
        _max = e
        _max_idx = i

dict = {
    0: "PROBRAIN",
    1: "GROW",
    2: "ARGOS",
    3: "ADMIN",
    4: "ANT",
    5: "MOTION",
    6: "SPG",
    7: "COMON",
    8: "ALMIGHTY",
}

print(dict[_max_idx])
