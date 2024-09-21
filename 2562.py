li = []
for _ in range(9):
    li.append(int(input()))

max_val = li[0]
max_idx = 0
for i in range(1, 9):
    if li[i] > max_val:
        max_val = li[i]
        max_idx = i

print(max_val)
print(max_idx + 1)
