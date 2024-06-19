from collections import deque
def solution(arr):
    answer = [0,0]
    for i in range (len(arr)):
        for j in range (len(arr[0])):
            if arr[i][j]:
                answer[1] +=1
            else:
                answer[0] += 1
    def isQuard(x,y,length):
        for i in range (x,x+length):
            for j in range (y,y+length):
                if arr[x][y] ^ arr[i][j]:                    
                    return False
        return True
    def in_range (nx,ny):
        return 0<=nx<len(arr)-1 and 0<=ny<len(arr)-1
    
    partlen = len(arr)
    queue = deque([(0,0,partlen)])
    while queue:
        x,y,partlen = queue.popleft()
        for dx,dy in  ((0,0),(0,1),(1,0),(1,1)):
            nx = x + dx * partlen
            ny = y + dy * partlen
            if in_range(nx,ny):
                if isQuard(nx,ny,partlen):
                    answer[arr[nx][ny]] -= (partlen ** 2 -1)
                else :
                    queue.append((nx,ny,partlen//2))
    return answer