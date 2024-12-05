from collections import Counter

n = int(input())
s = input()

li = [0] * 26
for c in s:
    if ord("a") <= ord(c) <= ord("z"):
        li[ord(c) - ord("a")] += 1

print(max(li))
