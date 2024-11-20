from collections import Counter

n = int(input())
s = input()

cnt = [0, 0, 0]
for i in range(n):
    if s[i] == "B":
        cnt[0] += 1
    elif s[i] == "S":
        cnt[1] += 1
    elif s[i] == "A":
        cnt[2] += 1

max_cnt = max(cnt)

if max_cnt == cnt[0] == cnt[1] == cnt[2]:
    print("SCU")
elif max_cnt == cnt[0] == cnt[1]:
    print("BS")
elif max_cnt == cnt[1] == cnt[2]:
    print("SA")
elif max_cnt == cnt[2] == cnt[0]:
    print("BA")
else:
    idx = cnt.index(max_cnt)
    if idx == 0:
        print("B")
    elif idx == 1:
        print("S")
    else:
        print("A")
