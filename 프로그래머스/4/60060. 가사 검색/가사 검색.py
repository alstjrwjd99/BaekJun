from collections import defaultdict

def solution(words, queries):
    answer = []

    forward_tries = defaultdict(dict)
    reverse_tries = defaultdict(dict)
    
    def insert(trie, word):
        cur = trie
        for w in word:
            cur.setdefault(w, [0, {}])
            cur[w][0] += 1
            cur = cur[w][1]
    
    def search(trie, query):
        cur = trie
        for q in query:
            if q == '?':
                return sum(node[0] for node in cur.values())
            if q not in cur:
                return 0
            cur = cur[q][1]
        return 0

    for word in words:
        length = len(word)
        insert(forward_tries[length], word)        
        insert(reverse_tries[length], word[::-1])  

    for query in queries:
        length = len(query)
        if length not in forward_tries:
            answer.append(0)
            continue
        
        if query[0] == '?': 
            result = search(reverse_tries[length], query[::-1])
        else:
            result = search(forward_tries[length], query)
        
        answer.append(result)
    
    return answer