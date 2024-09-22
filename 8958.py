t = int(input())

for _ in range(t):
    data = input()

    total_score = 0
    score = 0
    for char in data:
        if char == "O":
            score += 1
            total_score += score
        else:
            score = 0

    print(total_score)
