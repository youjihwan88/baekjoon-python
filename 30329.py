s = input()

cnt = 0
for i in range(len(s) - 3):
    if s[i] == "k" and s[i + 1] == "i" and s[i + 2] == "c" and s[i + 3] == "k":
        cnt += 1

print(cnt)
