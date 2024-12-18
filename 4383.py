import sys

lines = sys.stdin.readlines()
for line in lines:
    li = list(map(int, line.rstrip().split()))
    visited = [0] * li[0]
    b_fail = False

    for i in range(1, li[0] - 1):
        val = abs(li[i] - li[i + 1])
        if val >= li[0]:
            b_fail = True
            break

        if visited[val] == 0:
            visited[val] = 1
        else:
            b_fail = True
            break

    if b_fail:
        print("Not jolly")
    else:
        print("Jolly")
