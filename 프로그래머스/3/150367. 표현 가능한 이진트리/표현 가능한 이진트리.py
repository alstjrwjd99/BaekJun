def solution(numbers):
    answer = []
    
    def is_valid_tree(binary):
        length = len(binary)
        mid_idx = length // 2
    
        root = binary[mid_idx]
        left = binary[:mid_idx]
        right = binary[mid_idx + 1:]
        
        # 루트가 0인데 하위 트리에 1이 있으면 조건 위배
        if root == '0' and ('1' in left or '1' in right):
            return False
        
        if left and not is_valid_tree(left):
            return False
        if right and not is_valid_tree(right):
            return False
        
        return True
    
    for number in numbers:
        binary = bin(number)[2:]
        length = len(binary)
        padded_length = 2 ** (length.bit_length()) - 1
        binary = binary.zfill(padded_length)
        
        if is_valid_tree(binary):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer