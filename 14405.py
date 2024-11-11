import sys

s = input().rstrip()

i = 0
while True:
    if i == len(s):
        print("YES")
        sys.exit()
    if i + 1 < len(s) and s[i] == "p" and s[i + 1] == "i":
        i += 2
    elif i + 1 < len(s) and s[i] == "k" and s[i + 1] == "a":
        i += 2
    elif i + 2 < len(s) and s[i] == "c" and s[i + 1] == "h" and s[i + 2] == "u":
        i += 3
    else:
        print("NO")
        sys.exit()
