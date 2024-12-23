import sys

stk = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))
    if cmd[0] == 1:
        stk.append(cmd[1])
    elif cmd[0] == 2:
        if stk:
            print(stk.pop())
        else:
            print("-1")
    elif cmd[0] == 3:
        print(len(stk))
    elif cmd[0] == 4:
        if stk:
            print("0")
        else:
            print("1")
    elif cmd[0] == 5:
        if stk:
            print(stk[-1])
        else:
            print("-1")
