import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    s = sys.stdin.readline().rstrip()
    rst = ""
    for c in s:
        val = ord(c) + 1 if c != "Z" else ord("A")
        rst += chr(val)
    print(f"String #{i+1}")
    print(rst)
    print("")
