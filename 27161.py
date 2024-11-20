import sys

n = int(sys.stdin.readline().rstrip())

dir = 0
answer_t = 1
for _ in range(n):
    _watch, _t = sys.stdin.readline().rstrip().split()
    _t = int(_t)

    b_1 = False
    b_2 = False
    if _watch == "HOURGLASS":
        b_1 = True

    if _t == answer_t:
        b_2 = True

    b_yes = False
    if b_1 == True and b_2 == False:
        dir ^= 1
    elif b_1 == False and b_2 == True:
        b_yes = True

    print(f"{answer_t} {'YES' if b_yes else 'NO'}")

    if dir == 0:
        answer_t += 1
    else:
        answer_t -= 1
    if answer_t <= 0:
        answer_t += 12
    elif answer_t > 12:
        answer_t -= 12
