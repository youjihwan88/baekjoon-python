import sys

n = int(sys.stdin.readline().rstrip())

t1_score = 0
t2_scroe = 0

prev_state = 0

t1_time = 0
t2_time = 0
draw_time = 48 * 60

for _ in range(n):
    s_team, s_time = sys.stdin.readline().rstrip().split()
    team = int(s_team)
    time_h, time_m = map(int, s_time.split(":"))
    time = time_h * 60 + time_m

    if team == 1:
        t1_score += 1
    elif team == 2:
        t2_scroe += 1

    if t1_score > t2_scroe:
        state = 1
        t1_time += (60 * 48) - (time)
    elif t1_score < t2_scroe:
        state = 2
        t2_time += (60 * 48) - (time)
    else:
        state = 0
        draw_time += (60 * 48) - (time)

    if prev_state == 0:
        draw_time -= (60 * 48) - (time)
    elif prev_state == 1:
        t1_time -= (60 * 48) - (time)
    elif prev_state == 2:
        t2_time -= (60 * 48) - (time)

    prev_state = state

print(f"{t1_time//60:02d}:{t1_time%60:02d}")
print(f"{t2_time//60:02d}:{t2_time%60:02d}")
