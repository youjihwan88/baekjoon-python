r, c = map(int, input().split())
a, b = map(int, input().split())

for i in range(r):
    for _ in range(a):
        for j in range(c):
            if (i + j) % 2 == 0:
                print("X" * b, end="")
            else:
                print("." * b, end="")
        print("")
