n, m = map(int, input().split())

if n == 0 and m == 0:
    print("Not a moose")
elif n == m:
    print(f"Even {n*2}")
else:
    print(f"Odd {max(n,m)*2}")
