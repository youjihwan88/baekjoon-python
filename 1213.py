import sys
from collections import deque

li = [0] * 26
data = input()

for char in data:
    li[ord(char) - ord("A")] += 1

odd_cnt = 0
odd_cnt_char = ""

for i in range(len(li)):
    if li[i] % 2 == 1:
        odd_cnt += 1
        odd_cnt_char = chr(65 + i)

    if odd_cnt > 1:
        print("I'm Sorry Hansoo")
        sys.exit()

dq = deque()
if odd_cnt:
    dq.append(odd_cnt_char)
for i in range(len(li) - 1, -1, -1):
    for j in range(li[i] // 2):
        dq.append(chr(65 + i))
        dq.appendleft(chr(65 + i))

for i in range(len(dq)):
    print(dq[i], end="")
