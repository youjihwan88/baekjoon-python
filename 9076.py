import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    scores = list(map(int, sys.stdin.readline().rstrip().split()))
    scores.sort()
    _min = scores[1]
    _max = scores[-2]

    if _max - _min >= 4:
        print("KIN")
    else:
        print(sum(scores[1:-1]))
