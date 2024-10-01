str = input()

li = [0] * 26
for char in str:
    li[ord(char) - ord("a")] += 1

print(*li, sep=" ", end="")
