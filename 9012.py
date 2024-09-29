import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    in_data = sys.stdin.readline().rstrip()

    li = []
    b_fail = False
    for char in in_data:
        if char == "(":
            li.append(char)
        elif char == ")":
            if len(li) != 0 and li.pop() == "(":
                continue
            else:
                b_fail = True
                break

    if b_fail or len(li) != 0:
        print("NO")
    else:
        print("YES")
