n, k = map(int, input().split())
li = list(map(int, input().split()))
rst_li = [sum(li[0:k])]

for i in range(len(li)):
    if i + k >= len(li):
        break
    rst_li.append(rst_li[-1] + li[i + k] - li[i])

print(max(rst_li))
