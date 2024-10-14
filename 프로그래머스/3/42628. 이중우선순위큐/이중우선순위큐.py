import bisect

def solution(operations):
    queue = []
    for operation in operations:
        cmd,num = operation.split()
        num = int(num)
        if cmd == 'I':
            idx = bisect.bisect_left(queue, num)
            queue.insert(idx,num)
        else :
            if queue :
                if num == 1:
                    queue.pop()
                else : queue.pop(0)
    if queue: return [queue[-1], queue[0]]
    else :return [0,0]