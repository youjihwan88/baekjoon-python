n, m = map(int, input().split())
map = [[""] * m for _ in range(n)]
cnt_map1 = [[0] * m for _ in range(n)]
cnt_map2 = [[0] * m for _ in range(n)]

for i in range(n):
    _in = input()
    for j in range(m):
        map[i][j] = _in[j]

        if (i + j) % 2:  # odd number comb
            if map[i][j] == "W":
                cnt_map1[i][j] = 1
            else:
                cnt_map2[i][j] = 1
        else:  # even number comb
            if map[i][j] == "B":
                cnt_map1[i][j] = 1
            else:
                cnt_map2[i][j] = 1

rst = 64
for i in range(n + 1 - 8):
    for j in range(m + 1 - 8):
        cnt1 = 0
        cnt2 = 0
        for y in range(8):
            for x in range(8):
                cnt1 += cnt_map1[i + y][j + x]
                cnt2 += cnt_map2[i + y][j + x]
        rst = min(rst, cnt1, cnt2)

print(rst)
