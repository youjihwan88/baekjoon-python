li = list(map(int, input().split()))
hong = int(input())

grade = li.index(hong) + 1

if grade <= 5:
    print("A+")
elif grade <= 15:
    print("A0")
elif grade <= 30:
    print("B+")
elif grade <= 35:
    print("B0")
elif grade <= 45:
    print("C+")
elif grade <= 48:
    print("C0")
elif grade <= 50:
    print("F")
