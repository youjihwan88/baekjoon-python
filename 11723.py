import sys

m = int(sys.stdin.readline().rstrip())
s = set()
for _ in range(m):
    cmd = sys.stdin.readline().rstrip().split()
    if len(cmd) >= 2:
        val = int(cmd[1])

    if cmd[0] == "add":
        s.add(val)
    elif cmd[0] == "remove":
        s.discard(val)
    elif cmd[0] == "check":
        if val in s:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        if val in s:
            s.remove(val)
        else:
            s.add(val)
    elif cmd[0] == "all":
        s.update(range(1, 21))
    elif cmd[0] == "empty":
        s.clear()
