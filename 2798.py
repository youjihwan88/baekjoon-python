import sys

n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

rst = li[0] + li[1] + li[2]
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        for k in range(j + 1, len(li)):
            sum = li[i] + li[j] + li[k]

            if sum < m:
                if sum > rst:
                    rst = sum
            elif sum > m:
                break
            else:
                print(sum)
                sys.exit()

print(rst)
