def solution(board, h, w):
    answer = 0
    lenb = len(board)
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    for i in range (4):
        nx = h + dx[i]
        ny = w + dy[i]
        if 0 <= nx < lenb and  0 <= ny < lenb :
            if board[nx][ny] == board[h][w]:
                answer+=1
    return answer