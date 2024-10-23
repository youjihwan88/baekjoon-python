import sys

while True:
    line = sys.stdin.readline().rstrip()

    if line == "EOI":
        break

    line = line.lower()
    if "nemo" in line:
        print("Found")
    else:
        print("Missing")
