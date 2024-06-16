def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    global answer 
    answer = 0 

    def dfs(string):
        global answer 
        answer += 1 
        if string == word:
            return True
        if len(string) == 5:
            return False
        for alpha in alphabets:
            if dfs(string + alpha) == True:
                return True 

    for alpha in alphabets:
        if dfs(alpha) == True:
            return answer