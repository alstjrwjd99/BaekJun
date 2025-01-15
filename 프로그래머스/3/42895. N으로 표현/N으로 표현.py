def solution(N, number):
    if N == number :
        return 1
    answer = -1
    
    set_list = [set([int(str(N) * (i+1))]) for i in range (8)]
    
    for i in range (1,8):
        for j in range (i):
            for op1 in set_list[j]:
                for op2 in set_list[i-j-1]:
                    set_list[i].add(op1+op2)
                    set_list[i].add(op1-op2)
                    set_list[i].add(op1*op2)
                    if op2 != 0 :
                        set_list[i].add(op1//op2)
                        
        if number in set_list[i] :
            answer = i+1
            break
    
    return answer