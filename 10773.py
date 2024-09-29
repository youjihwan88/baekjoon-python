import sys

k = int(sys.stdin.readline().rstrip())
li = []
for _ in range(k):
    in_data = int(sys.stdin.readline().rstrip())
    if in_data == 0:
        li.pop()
    else:
        li.append(in_data)

print(sum(li))
