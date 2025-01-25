s = input()

idx1 = 0
idx2 = 0
for i, e in enumerate(s):
    if e == "(":
        idx1 = i
    elif e == ")":
        idx2 = i

if idx1 == len(s) - idx2 - 1:
    print("correct")
else:
    print("fix")
