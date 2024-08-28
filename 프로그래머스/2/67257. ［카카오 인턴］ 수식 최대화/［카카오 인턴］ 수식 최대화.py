from copy import deepcopy

def solution(expression):
    answer = 0
    operations = [('-','+','*'),('-','*','+'),('+','-','*'),('+','*','-'),('*','+','-'),('*','-','+')]
    
    def operate(num1, operator, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2    
        
    for operation in operations:
        nums = []
        ops = []
        num = ""
        
        # 숫자와 연산자 분리
        for ch in expression:
            if ch.isdigit():
                num += ch
            else:
                nums.append(int(num))
                ops.append(ch)
                num = ""
        nums.append(int(num))
        
        # 연산자 우선순위에 따라 계산
        for operator in operation:
            new_nums = []
            new_ops = []
            while ops:
                current_op = ops.pop(0)
                current_num = nums.pop(0)
                
                if current_op == operator:
                    next_num = nums.pop(0)
                    current_num = operate(current_num, current_op, next_num)
                    nums.insert(0, current_num)
                else:
                    new_nums.append(current_num)
                    new_ops.append(current_op)
            
            new_nums.append(nums.pop(0))
            nums = new_nums
            ops = new_ops
            
        answer = max(answer, abs(nums[0]))
                
    return answer