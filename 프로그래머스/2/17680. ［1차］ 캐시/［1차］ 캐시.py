from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue = deque(maxlen = cacheSize)
    for city in cities:
        city = city.lower()
        if city in queue:
            queue.remove(city)
            queue.append(city)
            answer += 1
        else :
            queue.append(city)
            answer += 5        
    return answer