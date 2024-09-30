import sys
import collections

n = int(sys.stdin.readline().rstrip())

queue = collections.deque()
for _ in range(n):
    in_data = sys.stdin.readline().rstrip().split()

    if in_data[0] == "push":
        queue.append(int(in_data[1]))
    elif in_data[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif in_data[0] == "size":
        print(len(queue))
    elif in_data[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif in_data[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif in_data[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
