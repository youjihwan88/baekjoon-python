import sys

n, h_atk = map(int, sys.stdin.readline().rstrip().split())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().rstrip().split())))


def check(max_hp):
    curr_hp = max_hp
    curr_atk = h_atk
    for t, a, h in li:
        if t == 1:
            if h % curr_atk == 0:
                needed_turn = h // curr_atk
            else:
                needed_turn = (h // curr_atk) + 1
            curr_hp -= (needed_turn - 1) * a
            if curr_hp <= 0:
                return False

        elif t == 2:
            curr_atk += a
            curr_hp += h
            curr_hp = min(max_hp, curr_hp)

    if curr_hp > 0:
        return True

    return False


l = 0
r = 999999000001 * 123456
rst = r

while l <= r:
    mid = (l + r) // 2
    if check(mid):
        rst = min(rst, mid)
        r = mid - 1
    else:
        l = mid + 1

print(rst)
