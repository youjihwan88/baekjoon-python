import sys

n = int(sys.stdin.readline().rstrip())

val = int(sys.stdin.readline().rstrip())
b_success = True
for _ in range(n - 1):
    x = int(sys.stdin.readline().rstrip())
    if x > val:
        b_success = False

if b_success:
    print("S")
else:
    print("N")
