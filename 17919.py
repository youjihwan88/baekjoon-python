s = input()

li = s.split()

cnt = 0
for e in li:
    if "ae" in e:
        cnt += 1

if cnt / len(li) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
