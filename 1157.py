li = [0] * 26

s = input()
for c in s:
    if ord("a") <= ord(c) <= ord("z"):
        li[ord(c) - ord("a")] += 1
    elif ord("A") <= ord(c) <= ord("Z"):
        li[ord(c) - ord("A")] += 1

max_val = 0
max_idx = 0
b_multi_return = False
for i, e in enumerate(li):
    if e > max_val:
        max_val = e
        max_idx = i
        b_multi_return = False
    elif e == max_val:
        b_multi_return = True

if b_multi_return:
    print("?")
else:
    print(chr(ord("A") + max_idx))
