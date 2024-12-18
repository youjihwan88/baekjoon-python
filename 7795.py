import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())

    li1 = list(map(int, sys.stdin.readline().rstrip().split()))
    li2 = list(map(int, sys.stdin.readline().rstrip().split()))

    li1.sort()
    li2.sort()

    j = 0
    cnt = 0
    for i in range(len(li2)):
        if j >= len(li1):
            break
        while True:
            if j >= len(li1):
                break

            if li1[j] <= li2[i]:
                j += 1
            else:
                cnt += len(li1) - j
                break

    print(cnt)
