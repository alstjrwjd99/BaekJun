import sys
input = sys.stdin.readline
from itertools import combinations

n, k = map(int, input().split())
words = []
can_speak = {'a', 'c', 'n', 't', 'i'}
required_chars = {'a', 'n', 't', 'i', 'c'}

if k < 5:
    print(0)
    sys.exit()

alpha_bits = 0
for char in required_chars:
    alpha_bits |= (1 << (ord(char) - ord('a')))

words_bits = []
for _ in range(n):
    word = input().strip()
    more = word[4:-4]
    word_bits = 0
    for char in more:
        word_bits |= (1 << (ord(char) - ord('a')))
    words_bits.append(word_bits)

remaining_chars = [chr(i + ord('a')) for i in range(26) if chr(i + ord('a')) not in required_chars]

max_count = 0

for combo in combinations(remaining_chars, k - 5):
    current_bits = alpha_bits
    for char in combo:
        current_bits |= (1 << (ord(char) - ord('a')))
    
    count = 0
    for word_bits in words_bits:
        if word_bits & current_bits == word_bits:
            count += 1
    
    max_count = max(max_count, count)

print(max_count)