'''
잘못된 경우
- 게임이 종료됐는데 X를 한번 더 친 경우
    -> 가로, 세로, 대각선 중에서 O로 이루어져 있는 곳이 있는지 파악 후 X 개수 >= O의 개수인 경우
- X부터 시작된 경우
    -> X개수 > O개수인 경우
'''

def solution(board):
    
    def was_end(board,shape):
        for i in board:
            if i == shape : return True
        
        for i in range (3):
            tmp = ''
            for j in range (3):
                tmp += board[j][i]
            if tmp == shape : return True
        
        if (board[0][0] + board[1][1] + board[2][2]) == shape : return True
        if (board[2][0] + board[1][1] + board[0][2]) == shape : return True
        
        return False
    
    def count_OX(board):
        o,x = 0,0
        for i in range (3):
            for j in range (3):
                if board[i][j] == 'O' : o += 1
                elif board[i][j] == 'X' : x += 1
        return o,x
    
    o_cnt,x_cnt = count_OX(board)
    
    if (o_cnt < x_cnt) : return 0
    if was_end(board, 'OOO') and o_cnt != x_cnt + 1 : return 0
    if was_end(board, 'XXX') and o_cnt != x_cnt : return 0
    if (o_cnt - x_cnt > 1) : return 0

    return 1