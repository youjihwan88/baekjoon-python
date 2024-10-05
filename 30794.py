in_data = input().split()
lv = int(in_data[0])
rst = in_data[1]

score = 0
if rst == "miss":
    score = 0
elif rst == "bad":
    score = lv * 200
elif rst == "cool":
    score = lv * 400
elif rst == "great":
    score = lv * 600
elif rst == "perfect":
    score = lv * 1000

print(score)
