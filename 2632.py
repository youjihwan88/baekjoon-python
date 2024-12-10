import sys
from collections import defaultdict

s = int(sys.stdin.readline().rstrip())
n, m = map(int, sys.stdin.readline().rstrip().split())
li_a = [0] * n
li_b = [0] * m
psum_a = [0]
psum_b = [0]
for i in range(n):
    li_a[i] = int(sys.stdin.readline().rstrip())
for i in range(m):
    li_b[i] = int(sys.stdin.readline().rstrip())


li_a *= 2
li_b *= 2

for i in range(2 * n):
    psum_a.append(psum_a[-1] + li_a[i])
for i in range(2 * m):
    psum_b.append(psum_b[-1] + li_b[i])

case_a = defaultdict(int)
case_b = defaultdict(int)

for size in range(1, n):
    for start in range(n):
        val = psum_a[start + size] - psum_a[start]
        case_a[val] += 1

case_a[psum_a[n] - psum_a[0]] += 1

for size in range(1, m):
    for start in range(m):
        val = psum_b[start + size] - psum_b[start]
        case_b[val] += 1

case_b[psum_b[m] - psum_b[0]] += 1

cnt = case_a[s] + case_b[s]
for i in range(1, s):
    cnt += case_a[i] * case_b[s - i]
print(cnt)
