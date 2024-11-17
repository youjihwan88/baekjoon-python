import sys

n = int(input())
li = [0] * (n + 1)
prime_num = []
for i in range(2, len(li)):
    if li[i] == 0:
        li[i] = 1
        prime_num.append(i)
        j = 2
        while i * j < len(li):
            li[i * j] = -1
            j += 1

s1 = 0
s2 = 0
if len(prime_num) == 0:
    print("0")
    sys.exit()
sum = prime_num[0]

cnt = 0
while True:
    if sum < n:
        s2 += 1
        if s2 >= len(prime_num):
            break
        sum += prime_num[s2]
    elif sum > n:
        sum -= prime_num[s1]
        s1 += 1
    else:
        cnt += 1
        sum -= prime_num[s1]
        s1 += 1
        s2 += 1
        if s2 >= len(prime_num):
            break
        sum += prime_num[s2]

    if s1 >= len(prime_num) or s2 >= len(prime_num):
        break

print(cnt)
