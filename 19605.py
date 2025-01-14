from collections import deque


t = input()
s = input()
dq = deque(s)

b_find = False
for i in range(len(s)):
    word = s[i:] + s[:i]

    if word in t:
        b_find = True
        break

if b_find:
    print("yes")
else:
    print("no")
