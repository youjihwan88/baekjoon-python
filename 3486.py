import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    s1, s2 = sys.stdin.readline().rstrip().split()

    rst = int(s1[::-1]) + int(s2[::-1])
    rst = int(str(rst)[::-1])
    print(rst)
