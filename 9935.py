import sys

s1 = input()
s2 = input()

li = []

for c in s1:
    li.append(c)

    b_fail = False
    if len(li) < len(s2):
        b_fail = True
    else:
        for i in range(len(s2)):
            if li[-(i + 1)] != s2[-(i + 1)]:
                b_fail = True
                break

    if not b_fail:
        for i in range(len(s2)):
            li.pop()

if len(li) == 0:
    print("FRULA")
else:
    print(*li, sep="")
