score = input()
val = 0.0

if score == "A+":
    val = 4.3
elif score == "A0":
    val = 4.0
elif score == "A-":
    val = 3.7
elif score == "B+":
    val = 3.3
elif score == "B0":
    val = 3.0
elif score == "B-":
    val = 2.7
elif score == "C+":
    val = 2.3
elif score == "C0":
    val = 2.0
elif score == "C-":
    val = 1.7
elif score == "D+":
    val = 1.3
elif score == "D0":
    val = 1.0
elif score == "D-":
    val = 0.7

print(f"{val:0.1f}")
