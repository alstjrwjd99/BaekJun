x,y,w,s = map(int,input().split())

def cal_min(x,y,w,s):
  #직선거리로만 이동
  dis_1 = (x+y) * w
  #대각전으로만 이동
  if (x+y) % 2 ==0 :
    dis_2 = max(x,y) * s
  #대각인데 변이하나 남는 경우
  else :
    dis_2 = (max(x,y) - 1) * s + w
  #대각 + 평행 max(대각)
  dis_3 = min(x,y)*s + abs(x-y)*w

  return min(dis_1,dis_2,dis_3)

print(cal_min(x,y,w,s))