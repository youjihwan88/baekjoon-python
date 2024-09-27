import collections

n = int(input())
dq = collections.deque()
for i in range(n):
    dq.append(n - i)


while True:
    if len(dq) == 1:
        break

    dq.pop()
    dq.rotate(1)

print(dq[0])
