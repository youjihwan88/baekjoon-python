answer = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
]

n = int(input())
b_yes = False
for _ in range(n):
    s = input()
    if s not in answer:
        b_yes = True
        break

if b_yes:
    print("Yes")
else:
    print("No")
