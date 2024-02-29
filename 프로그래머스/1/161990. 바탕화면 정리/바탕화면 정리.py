def solution(wallpaper):
    answer = []
    len_h = len(wallpaper)
    len_w = len(wallpaper[0])
    lux,luy = len_h,len_w
    rdx,rdy = 0,0
    for i in range (len_h):
        for j in range(len_w):
            if wallpaper[i][j] == '#':
                lux,luy = min(i,lux),min(j,luy)
                rdx,rdy = max(i,rdx),max(j,rdy)
                
                answer = [lux,luy,rdx+1,rdy+1]
    return answer