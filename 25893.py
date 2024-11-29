import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    cnt = 0
    for e in li:
        if e >= 10:
            cnt += 1

    print(*li, sep=" ")
    if cnt == 0:
        print("zilch")
    elif cnt == 1:
        print("double")
    elif cnt == 2:
        print("double-double")
    elif cnt == 3:
        print("triple-double")
    print("")
