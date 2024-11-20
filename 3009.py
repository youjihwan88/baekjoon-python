from collections import Counter

x_li = []
y_li = []

for i in range(3):
    a, b = map(int, input().split())
    x_li.append(a)
    y_li.append(b)


x_counter = Counter(x_li)
y_counter = Counter(y_li)

for k, v in x_counter.items():
    if v == 1:
        x = k

for k, v in y_counter.items():
    if v == 1:
        y = k

print(f"{x} {y}")
