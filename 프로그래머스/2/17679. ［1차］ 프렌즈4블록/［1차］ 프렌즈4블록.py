from functools import cmp_to_key
bucket = []
def cmp(x,y):
    if x[0] > y[0]:
        return 1
    elif x[0]==y[0]:
        if x[1] > y[1]:
            return 1
        else:
            return -1
    else:
        return -1
def dynamic(m,n,board):
    global bucket
    distance = [(-1,1),(-1,0),(0,1)]
    stack = []
    for x in range(1,n):
        for y in range(len(bucket[x])-2,-1,-1):
            (i,j) = bucket[x][y]
            tmp = [(x,y)]
            for d in range(len(distance)):# bucket관점...
                (dx,dy) = distance[d]
                if y+dy >= len(bucket[x+dx]):

                    break
                (a,b)=bucket[x+dx][y+dy]
                if board[b][a]==board[j][i]:
                    tmp.append((x+dx,y+dy))
            if len(tmp)==4:
                stack+=tmp
    stack = list(set(stack))
    count = len(stack)
    if count==0:
        return count
    s = sorted(stack,key=cmp_to_key(cmp))

    while len(s)!=0:
        (x,y) = s.pop()
        bucket[x].pop(y)
    return count

def solution(m, n, board):
    global bucket
    answer = 0
    bucket = [[(i,j) for j in range(m-1,-1,-1)] for i in range(n)]
    delete=1
    while delete!=0:
        delete = dynamic(m,n,board)
        answer+=delete 
    return answer
