import sys

while True:
    name, age, weight = sys.stdin.readline().rstrip().split()

    if name == "#" and age == "0" and weight == "0":
        break

    b_junior = True
    if int(age) > 17 or int(weight) >= 80:
        b_junior = False

    if b_junior:
        print(f"{name} Junior")
    else:
        print(f"{name} Senior")
