while True:
    s = input()

    if s == "0":
        break

    b_palindrome = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            b_palindrome = False
            break

    if b_palindrome:
        print("yes")
    else:
        print("no")
