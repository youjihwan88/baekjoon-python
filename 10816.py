n = int(input())
dict = {}
in_data = map(int, input().split())
for e in in_data:
    if dict.get(e) is not None:
        dict[e] += 1
    else:
        dict[e] = 1


m = int(input())
find_data = map(int, input().split())
for e in find_data:
    if dict.get(e) is not None:
        print(dict[e], end=" ")
    else:
        print(0, end=" ")
