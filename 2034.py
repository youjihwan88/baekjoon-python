import sys

piano_plus = [2, 1, 2, 2, 1, 2, 2]
piano_minus = [2, 2, 1, 2, 2, 1, 2]
n = int(sys.stdin.readline().rstrip())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().rstrip()))

rst = []
# A, B, C, D, E, F, G
for i in range(7):
    b_fail = False

    start = i
    curr = i
    for e in li:
        if b_fail:
            break

        val = e
        if val < 0:
            val *= -1
            while True:
                if val == 0:
                    break
                elif val < 0:
                    b_fail = True
                    break
                val -= piano_minus[curr]
                curr -= 1
                if curr < 0:
                    curr += 7
        else:
            while True:
                if val == 0:
                    break
                elif val < 0:
                    b_fail = True
                    break
                val -= piano_plus[curr]
                curr += 1
                if curr >= 7:
                    curr -= 7

        if curr < 0:
            curr += 7
        elif curr >= 7:
            curr -= 7

    if b_fail:
        continue
    else:
        rst.append([chr(ord("A") + start), chr(ord("A") + curr)])

for e in rst:
    print(*e, sep=" ")
