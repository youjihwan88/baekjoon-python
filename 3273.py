n = int(input())
li = list(map(int, input().split()))
x = int(input())

li.sort()

s = 0
e = len(li) - 1

cnt = 0
while True:
    if s >= e:
        break

    sum = li[s] + li[e]
    if sum == x:
        s += 1
        e -= 1
        cnt += 1
    elif sum > x:
        e -= 1
    elif sum < x:
        s += 1

print(cnt)
