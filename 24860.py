import sys

vk, jk = map(int, sys.stdin.readline().rstrip().split())
vl, jl = map(int, sys.stdin.readline().rstrip().split())
vh, dh, jh = map(int, sys.stdin.readline().rstrip().split())

print(vh * dh * jh * (vl * jl + vk * jk))
