import sys
N = int(sys.stdin.readline())
queue = []
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        queue.insert(0, order[1])
    elif order[0] == "pop":
        if len(queue) != 0: print(queue.pop())
        else: print(-1)
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        if len(queue) == 0: print(1)
        else : print(0)
    elif order[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue) -1])
    elif order[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[0])
