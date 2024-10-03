n = int(input())

cnt = 0
for _ in range(n):
    word = input()

    li = []
    for char in word:
        if len(li) != 0 and li[-1] == char:
            li.pop()
        else:
            li.append(char)

    if len(li) == 0:
        cnt += 1

print(cnt)
