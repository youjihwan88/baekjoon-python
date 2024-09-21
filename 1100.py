cnt = 0

for i in range(8):
    str = input()
    for j in range(len(str)):
        if (i + j) % 2 == 0 and str[j] == "F":
            cnt += 1

print(cnt)
