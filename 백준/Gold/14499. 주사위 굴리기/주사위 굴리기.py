# 입력받기
import sys
input = sys.stdin.readline
N,M,x,y,cmd = map(int,input().split())
board = []
for _ in range (N):
    board.append(list(map(int,input().split())))
direct = list(map(int,input().split()))

# 1:동 2:서 3:북 4:남 
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

# 상, 우, 앞
urf = [1,3,5]
dice = [0] * 7

def new_urf(direction, urf):
    u,r,f = urf[0],urf[1],urf[2]
    if direction == 1:
        urf = [7-r,u,f]
    elif direction == 2:
        urf = [r,7-u,f]
    elif direction == 3:
        urf = [f,r,7-u]
    elif direction == 4:
        urf = [7-f,r,u]
    return urf

for i in direct:
    x,y = x+dx[i], y+dy[i]
    # 범위 밖으로 넘어가면 무시
    if x < 0 or x >= N or y < 0 or y >= M :
        x,y = x-dx[i], y-dy[i]
        continue
    # 현재 구른 상태의 주사위
    urf = new_urf(i,urf)
    # board가 0이면 주사위 밑면에 있는 숫자가 복사 board[x][y] = dice[]
    if board[x][y]==0:
        board[x][y] = dice[7-urf[0]]
        print(dice[urf[0]])
    # board가 0이 아니면 dice[] = board[x][y] 고 board[x][y] = 0이 됨
    else:
        dice[7-urf[0]] = board[x][y]
        board[x][y] = 0
        print(dice[urf[0]])
        