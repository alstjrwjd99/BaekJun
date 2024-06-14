from collections import deque
def solution(x, y, n):
    answer = 0
    if x == y:
        return 0
    dup = set()
    queue = deque([(x,0)])
    dup.add(x)
    while queue:
        nx,cnt = queue.popleft()
        if nx+n not in dup and nx+n < y:
            queue.append((nx+n,cnt+1))
            dup.add(nx+n)
        elif nx+n == y:
            return cnt+1
        if nx*2 not in dup and nx*2 < y:
            queue.append((nx*2,cnt+1))
            dup.add(nx*2)
        elif nx*2 == y:
            return cnt+1
        if nx*3 not in dup and nx*3 < y:
            queue.append((nx*3,cnt+1))
            dup.add(nx*3)
        elif nx*3 == y:
            return cnt+1
    return -1