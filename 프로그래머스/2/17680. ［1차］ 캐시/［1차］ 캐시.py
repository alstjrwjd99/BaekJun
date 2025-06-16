'''
hash map -> city : node
링크드 리스트 사용
'''
class Node :
    def __init__(self,key) :
        self.key = key
        self.prev = None
        self.next = None

class LRUCache :
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.time = 0

        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_front_tail(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail

        self.tail.prev = node

    def put(self, key):
        if key in self.cache :
            node = self.cache[key]
            self.remove(node)
            self.time += 1
        else : self.time += 5

        node = Node(key)
        self.cache[key] = node
        self.add_front_tail(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
    
    def get_time(self):
        return self.time
        
def solution(cacheSize, cities):
    lru = LRUCache(cacheSize)
    for city in cities :
        lru.put(city.lower())
    return lru.get_time()