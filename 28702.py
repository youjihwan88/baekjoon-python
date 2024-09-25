a = input()
b = input()
c = input()

rst = 0
if a.isdecimal():
    rst = int(a) + 3
elif b.isdecimal():
    rst = int(b) + 2
elif c.isdecimal():
    rst = int(c) + 1

if rst % 3 == 0:
    if rst % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif rst % 5 == 0:
    print("Buzz")
else:
    print(rst)
