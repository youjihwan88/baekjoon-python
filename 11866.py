import collections

n, k = map(int, input().split())

dq = collections.deque()
for i in range(n):
    dq.append(n - i)

rst = []
while len(dq):
    dq.rotate(k - 1)
    rst.append(str(dq.pop()))

print("<", end="")
print(", ".join(rst), end="")
print(">", end="")
