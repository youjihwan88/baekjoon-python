li = list(map(int, input().split()))

b_asc = True
b_des = True

for i in range(8):
    if li[i] != i + 1:
        b_asc = False

    if li[i] != 8 - i:
        b_des = False

    if not b_asc and not b_des:
        break

if b_asc:
    print("ascending")
elif b_des:
    print("descending")
else:
    print("mixed")
