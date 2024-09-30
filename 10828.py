import sys

n = int(sys.stdin.readline().rstrip())

stk = []
for _ in range(n):
    in_data = sys.stdin.readline().rstrip().split()

    if in_data[0] == "push":
        stk.append(int(in_data[1]))
    elif in_data[0] == "pop":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif in_data[0] == "size":
        print(len(stk))
    elif in_data[0] == "empty":
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif in_data[0] == "top":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])
