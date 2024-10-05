max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

in_data = list(map(int, input().split()))

if sum(in_data) < 100:
    print("none")
else:
    b_hacker = False
    for i in range(9):
        if in_data[i] > max_score[i]:
            b_hacker = True
            break

    if b_hacker:
        print("hacker")
    else:
        print("draw")
