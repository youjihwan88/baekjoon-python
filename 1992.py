import sys

sys.setrecursionlimit(10**6)


# def search(_map):
#     if len(_map) == 1:
#         return str(_map[0][0])

#     rst = "("
#     n = len(_map) // 2

#     # left-top
#     b_all_same = True
#     val = _map[0][0]
#     for i in range(n):
#         for j in range(n):
#             if _map[i][j] != val:
#                 b_all_same = False
#                 break
#     if b_all_same:
#         rst += str(val)
#     else:
#         rst += search([_map[i][0:n] for i in range(0, n)])

#     # right-top
#     b_all_same = True
#     val = _map[0][n]
#     for i in range(n):
#         for j in range(n, 2 * n):
#             if _map[i][j] != val:
#                 b_all_same = False
#                 break
#     if b_all_same:
#         rst += str(val)
#     else:
#         rst += search([_map[i][n : 2 * n] for i in range(0, n)])

#     # left-bottom
#     b_all_same = True
#     val = _map[n][0]
#     for i in range(n, 2 * n):
#         for j in range(n):
#             if _map[i][j] != val:
#                 b_all_same = False
#                 break
#     if b_all_same:
#         rst += str(val)
#     else:
#         rst += search([_map[i][0:n] for i in range(n, 2 * n)])

#     # right-bottom
#     b_all_same = True
#     val = _map[n][n]
#     for i in range(n, 2 * n):
#         for j in range(n, 2 * n):
#             if _map[i][j] != val:
#                 b_all_same = False
#                 break
#     if b_all_same:
#         rst += str(val)
#     else:
#         rst += search([_map[i][n : 2 * n] for i in range(n, 2 * n)])

#     rst += ")"
#     return rst


def search(_map):
    n = len(_map)

    b_all_same = True
    val = _map[0][0]
    for i in range(n):
        for j in range(n):
            if _map[i][j] != val:
                b_all_same = False
                break

    if b_all_same:
        return str(val)

    rst = "("
    rst += search([_map[i][0 : n // 2] for i in range(n // 2)])
    rst += search([_map[i][n // 2 : n] for i in range(n // 2)])
    rst += search([_map[i][0 : n // 2] for i in range(n // 2, n)])
    rst += search([_map[i][n // 2 : n] for i in range(n // 2, n)])
    rst += ")"
    return rst


n = int(sys.stdin.readline().rstrip())
_map = [[0] * n for _ in range(n)]
for i in range(n):
    in_data = sys.stdin.readline().rstrip()
    for j in range(n):
        _map[i][j] = int(in_data[j])

print(search(_map))
