import sys

n = int(sys.stdin.readline().rstrip())
op = []
stk = []

val = 1
b_fail = False
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    while x >= val:
        stk.append(val)
        op.append("+")
        val += 1

    if len(stk) and stk[-1] == x:
        stk.pop()
        op.append("-")
    else:
        b_fail = True
        break

if not b_fail:
    print("\n".join(op))
else:
    print("NO")
