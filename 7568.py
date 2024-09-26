n = int(input())

li = [[0, 0] for _ in range(n)]
for i in range(n):
    li[i][0], li[i][1] = map(int, input().split())

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue

        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            rank += 1
    print(rank, end=" ")
