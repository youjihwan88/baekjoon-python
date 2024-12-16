p, w = map(int, input().split())
s = input()

alp_to_num = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
alp_score = [
    p,
    2 * p,
    3 * p,
    p,
    2 * p,
    3 * p,
    p,
    2 * p,
    3 * p,
    p,
    2 * p,
    3 * p,
    p,
    2 * p,
    3 * p,
    p,
    2 * p,
    3 * p,
    4 * p,
    p,
    2 * p,
    3 * p,
    p,
    2 * p,
    3 * p,
    4 * p,
]

prev_state = 0
rst = 0
for c in s:
    if c == " ":
        curr_state = 0
        rst += p
    else:
        curr_state = alp_to_num[ord(c) - ord("A")]
        rst += alp_score[ord(c) - ord("A")]

    if curr_state == prev_state and curr_state != 0:
        rst += w

    prev_state = curr_state


print(rst)
