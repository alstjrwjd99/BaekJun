import sys
input = sys.stdin.readline

FIRST = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
QUESTION = '"재귀함수가 뭔가요?"'
STORY = [
    '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
    '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
    '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
]
ANSWER = '"재귀함수는 자기 자신을 호출하는 함수라네"'
END_SENTENCE = '라고 답변하였지.'

def chatbot(k, n):
    indent = '____' * k
    
    if k == n:
        return f'{indent}{QUESTION}\n{indent}{ANSWER}\n{indent}{END_SENTENCE}'
    
    current_sentence = f'{indent}{QUESTION}\n' + '\n'.join([f'{indent}{line}' for line in STORY]) + '\n'
    next_sentence = chatbot(k + 1, n)
    
    return current_sentence + next_sentence + f'\n{indent}{END_SENTENCE}'

n = int(input())

print(FIRST)
print(chatbot(0, n))