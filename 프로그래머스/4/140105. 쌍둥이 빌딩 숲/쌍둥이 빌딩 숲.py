MODULAR_ARITHMETIC_DIVIDE_NUMBER = 1000000007

def solution(n, count):
    arr = [[0] * (n+1) for _ in range (n+1)]
    arr[1][1] = 1
    
    for row in range (2, n+1):
        prevRow = row - 1
        for col in range (1,row+1):
            arr[row][col] = (arr[prevRow][col - 1] + 2 * prevRow * arr[prevRow][col]) % MODULAR_ARITHMETIC_DIVIDE_NUMBER
    
    return arr[n][count]