def solution(s):
    answer = [0,0]
    def removeZeroAndBinary (n):
        one = n.count('1')
        answer[0] += 1
        answer[1] += n.count('0')
        if one == 1:
            return
        return removeZeroAndBinary(bin(one)[2:])
    removeZeroAndBinary(s)
    
    return answer