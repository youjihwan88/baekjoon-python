li = ["K", "O", "R", "E", "A"]
i = 0

s = input()
cnt = 0
for c in s:
    if c == li[i % 5]:
        i += 1

print(i)
