import sys

n = int(sys.stdin.readline().rstrip())

st = set()
for _ in range(n):
    st.add(sys.stdin.readline().rstrip())
rst = sorted(st, key=lambda x: (len(x), x))

print(*rst, sep="\n")
