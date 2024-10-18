def solution(numbers, target):
    
    def dfs(idx, result):
        if idx == len(numbers):
            return 1 if result == target else 0
        
        return dfs(idx + 1, result + numbers[idx]) + dfs(idx + 1, result - numbers[idx])
    
    return dfs(0, 0)