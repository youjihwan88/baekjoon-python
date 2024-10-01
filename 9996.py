n = int(input())
s_word, e_word = input().split("*")

for _ in range(n):
    data = input()
    if data.startswith(s_word) and data.endswith(e_word) and len(data) >= len(s_word) + len(e_word):
        print("DA")
    else:
        print("NE")
