s = input()

cnt = 0
i = 0
while True:
    if i >= len(s):
        break
    try:
        if s[i] == "c" and s[i + 1] == "=":
            cnt += 1
            i += 2
        elif s[i] == "c" and s[i + 1] == "-":
            cnt += 1
            i += 2
        elif s[i] == "d" and s[i + 1] == "z" and s[i + 2] == "=":
            cnt += 1
            i += 3
        elif s[i] == "d" and s[i + 1] == "-":
            cnt += 1
            i += 2
        elif s[i] == "l" and s[i + 1] == "j":
            cnt += 1
            i += 2
        elif s[i] == "n" and s[i + 1] == "j":
            cnt += 1
            i += 2
        elif s[i] == "s" and s[i + 1] == "=":
            cnt += 1
            i += 2
        elif s[i] == "z" and s[i + 1] == "=":
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    except IndexError as e:
        cnt += 1
        i += 1

print(cnt)
