import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
s1 = set()
s2 = set()

for i in range(n):
    s1.add(sys.stdin.readline().rstrip())
for j in range(m):
    s2.add(sys.stdin.readline().rstrip())

li = list(s1.intersection(s2))
li.sort()
print(len(li))
print(*li, sep="\n")
