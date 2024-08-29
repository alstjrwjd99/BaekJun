def ranking(n): 
    if n == 6 :
      rank = 1
    elif n == 5 :
      rank = 2
    elif n == 4 :
      rank = 3    
    elif n == 3 :
      rank = 4    
    elif n == 2 :
      rank = 5
    else : rank = 6
    return rank

def solution(lottos, win_nums):
    cnt = 0
    plusminus = 0
    for i in range(6):
      for j in  range(6): 
        if lottos[i] == win_nums[j]: 
          cnt += 1
      if lottos[i] == 0 :
        plusminus += 1
    maxans = ranking(cnt + plusminus)
    minans = ranking(cnt)
    answer = [maxans,minans]
    return answer