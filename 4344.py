import sys
import statistics

c = int(sys.stdin.readline().rstrip())
for _ in range(c):
    li = list(map(int, sys.stdin.readline().rstrip().split()))

    mean = statistics.mean(li[1:])
    cnt = 0
    for i in range(1, len(li)):
        if li[i] > mean:
            cnt += 1

    print(f"{cnt/(len(li)-1)*100}%")
