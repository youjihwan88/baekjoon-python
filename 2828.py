n, m = map(int, input().split())
j = int(input())

s_idx = 1
e_idx = m

cnt = 0
for _ in range(j):
    apple = int(input())

    if apple >= s_idx and apple <= e_idx:
        continue
    elif apple < s_idx:
        dist = s_idx - apple
        cnt += dist
        s_idx -= dist
        e_idx -= dist
    elif apple > e_idx:
        dist = apple - e_idx
        cnt += dist
        s_idx += dist
        e_idx += dist

print(cnt, end="")
