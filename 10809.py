li = [-1] * 26

word = input()
for i, c in enumerate(word):
    if li[ord(c) - 97] != -1:
        continue

    li[ord(c) - 97] = i

for l in li:
    print(l, end=" ")
