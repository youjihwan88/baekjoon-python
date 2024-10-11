h = int(input())

rst = ""
if h == 0:
    rst = "1"
elif h == 1:
    rst = "0"
elif h % 2 == 0:
    rst = "8" * (h // 2)
elif h % 2 == 1:
    rst = "4" + "8" * (h // 2)

print(rst)
