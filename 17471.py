import sys

n = int(sys.stdin.readline().rstrip())
n_human = list(map(int, sys.stdin.readline().rstrip().split()))
adj_li = []
min_pop = 100 * 10
for _ in range(n):
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    adj_li.append([li[i] - 1 for i in range(1, len(li))])


def dfs(here, visited, team):
    for there in adj_li[here]:
        if visited[there] == team:
            visited[there] = 1
            dfs(there, visited, team)
    return


def check(li_a, li_b):
    if len(li_a) == 0 or len(li_b) == 0:
        return False

    visited = [0] * n
    for e in li_a:
        visited[e] = "A"
    for e in li_b:
        visited[e] = "B"

    visited[li_a[0]] = 1
    visited[li_b[0]] = 1

    dfs(li_a[0], visited, "A")
    dfs(li_b[0], visited, "B")

    for i in range(n):
        if visited[i] != 1:
            return False

    return True


b_success = False
for i in range(1 << n):
    # 선거구 나누기(a / b 선거구)
    li_a = []
    li_b = []
    for j in range(n):
        if i & (1 << j):
            li_a.append(j)
        else:
            li_b.append(j)

    # 인접한 구역인지 확인
    if not check(li_a, li_b):
        continue

    # 인구 차이 계산
    b_success = True
    cnt_a = 0
    cnt_b = 0
    for e in li_a:
        cnt_a += n_human[e]
    for e in li_b:
        cnt_b += n_human[e]
    min_pop = min(abs(cnt_a - cnt_b), min_pop)
    if min_pop == 0:
        break

if not b_success:
    print("-1")
else:
    print(min_pop)
