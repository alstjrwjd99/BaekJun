def solution(s):
    def compress(s, length):
        compressed = []
        prev = s[:length]
        count = 1
        
        for i in range(length, len(s), length):
            current = s[i:i+length]
            if current == prev:
                count += 1
            else:
                if count > 1:
                    compressed.append(str(count))
                compressed.append(prev)
                prev = current
                count = 1
        
        if count > 1:
            compressed.append(str(count))
        compressed.append(prev)
        
        return ''.join(compressed)
    
    answer = len(s)
    for length in range(1, len(s) // 2 + 1):
        compressed_string = compress(s, length)
        answer = min(answer, len(compressed_string))
    
    return answer