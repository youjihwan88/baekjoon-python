import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
_map = []
chicken_li = []
home_li = []


def get_chicken_distance(home_li, chicken_li):
    city_chicken_distance = 0
    for home_y, home_x in home_li:
        chicken_distance = n * n
        for chicken_y, chicken_x in chicken_li:
            chicken_distance = min(abs(home_y - chicken_y) + abs(home_x - chicken_x), chicken_distance)

        city_chicken_distance += chicken_distance

    return city_chicken_distance


for i in range(n):
    _map.append(list(map(int, sys.stdin.readline().rstrip().split())))

    for j in range(n):
        if _map[i][j] == 2:
            chicken_li.append((i, j))
        elif _map[i][j] == 1:
            home_li.append((i, j))

min_chicken_distance = n * n * len(home_li)

for selected_chickens in combinations(chicken_li, m):
    chicken_distance = get_chicken_distance(home_li, selected_chickens)
    min_chicken_distance = min(chicken_distance, min_chicken_distance)


print(min_chicken_distance)
