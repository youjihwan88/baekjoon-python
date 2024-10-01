sentence = input()
encoded = ""

for i in range(len(sentence)):
    char = ""
    if ord(sentence[i]) >= ord("a") and ord(sentence[i]) <= ord("z"):
        char = ord(sentence[i]) + 13
        if char > ord("z"):
            char -= 26
        char = chr(char)
    elif ord(sentence[i]) >= ord("A") and ord(sentence[i]) <= ord("Z"):
        char = ord(sentence[i]) + 13
        if char > ord("Z"):
            char -= 26
        char = chr(char)
    else:
        char = sentence[i]

    encoded += char

print(encoded)
