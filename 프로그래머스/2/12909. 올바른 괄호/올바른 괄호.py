def solution(s):
    answer = True
    stack = []
    for i in s :
        try :
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
        except:
            return False

    if stack : return False
    else : return True