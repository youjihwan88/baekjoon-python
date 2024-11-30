n = int(input())

inc = 1

prev_i = 0
curr_i = 0
while True:
    curr_i += inc
    if prev_i < n <= curr_i:
        sum = inc + 1
        idx = n - prev_i
        if inc % 2 == 0:
            print(f"{idx}/{sum-idx}")
        else:
            print(f"{sum-idx}/{idx}")
        break

    prev_i = curr_i
    inc += 1
