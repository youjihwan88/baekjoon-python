from collections import Counter

n = int(input())
li = list(map(int, input().split()))

c = Counter(li)
print(max(c.values()))
