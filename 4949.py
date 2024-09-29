import sys

while True:
    in_data = sys.stdin.readline().rstrip()

    if in_data == ".":
        break

    li = []
    b_fail = False
    for char in in_data:
        if char == "(" or char == "[":
            li.append(char)
        elif char == ")":
            if len(li) == 0 or li.pop() != "(":
                b_fail = True
                break
        elif char == "]":
            if len(li) == 0 or li.pop() != "[":
                b_fail = True
                break

    if b_fail or len(li) != 0:
        print("no")
    else:
        print("yes")
