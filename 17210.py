n = int(input())
a = int(input())

if n >= 6:
    print("Love is open door")
else:
    for i in range(1, n):
        a = 1 - a
        print(a)
