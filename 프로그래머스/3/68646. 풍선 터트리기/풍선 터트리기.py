# 양 옆에 자기보다 작은 수가 있으면 안됨
# 예를 들어 오른쪽에 가장 작은 수가 있으면 그 숫자보다 큰애는 다 터트리고 마지막에 그 가장 작은 수를 터트리면 됨
# 이러면 왼쪽에 자기보다 작은 숫자가 있는 경우 못 터트림
# -> 즉 맨 왼쪽과 맨 오른쪽은 항상 가능하다는 소리

# [-16, 27, 65, -2, 58,-92,-71,-68,-61,-33]	
# [-16,-16,-16,-16,-16,-92,-92,-92,-92,-92]
# [-92,-92,-92,-92,-92,-92,-71,-68,-61,-33]

def solution(a):
    answer = len(a)
    left_min = []
    mini = float('inf')
    for i in a:
        mini = min(mini, i)
        left_min.append(mini)
    
    mini = float('inf')
    right_min = []
    for i in range(len(a)-1,-1,-1):
        mini = min(mini, a[i])
        right_min.append(mini)
    right_min = right_min[::-1]
    
    for i in range (len(a)):
        if (a[i] > left_min[i] and a[i] > right_min[i]) : answer -= 1        
    
    return answer
