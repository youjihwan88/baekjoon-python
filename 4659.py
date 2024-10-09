import sys

while True:
    in_data = sys.stdin.readline().rstrip()

    if in_data == "end":
        break

    b_contains_vowel = False
    b_fail = False
    successive_vowel_cnt = 0
    successive_consonant_cnt = 0
    prev_char = " "
    for i, c in enumerate(in_data):
        if c in ["a", "i", "e", "o", "u"]:
            b_contains_vowel = True
            successive_vowel_cnt += 1
            successive_consonant_cnt = 0
        else:
            successive_consonant_cnt += 1
            successive_vowel_cnt = 0

        if successive_consonant_cnt >= 3 or successive_vowel_cnt >= 3:
            b_fail = True
            break

        if c == prev_char and c not in ["e", "o"]:
            b_fail = True
            break

        prev_char = c

    if b_contains_vowel and not b_fail:
        print(f"<{in_data}> is acceptable.")
    else:
        print(f"<{in_data}> is not acceptable.")
