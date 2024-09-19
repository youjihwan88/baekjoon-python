students = [0] * 30

for _ in range(28):
    idx = int(input()) - 1
    students[idx] = 1

for i in range(30):
    if students[i] == 0:
        print(i + 1)
