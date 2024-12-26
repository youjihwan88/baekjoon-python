s = input()

li = [0] * 26
for c in s:
    li[ord(c) - ord("a")] += 1

odd_cnt = 0
for i in li:
    if i % 2 != 0:
        odd_cnt += 1

rst = 0
if odd_cnt > 1:
    rst += odd_cnt - 1

print(rst)
