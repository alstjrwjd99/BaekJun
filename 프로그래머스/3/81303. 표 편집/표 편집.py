class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

def solution(n, k, cmd):
    # 노드 초기화
    nodes = [Node(i) for i in range(n)]
    for i in range(1, n):
        nodes[i - 1].next = nodes[i]
        nodes[i].prev = nodes[i - 1]

    # 헤드와 포인터 설정
    head = nodes[0]  # 시작(head)
    pointer = nodes[k]
    stack = []  # 삭제된 노드를 저장할 스택

    # 명령 처리
    for c in cmd:
        command = c.split()
        if command[0] == "U":  # 위로 이동
            x = int(command[1])
            for _ in range(x):
                if pointer.prev:
                    pointer = pointer.prev
        elif command[0] == "D":  # 아래로 이동
            x = int(command[1])
            for _ in range(x):
                if pointer.next:
                    pointer = pointer.next
        elif command[0] == "C":  # 삭제
            stack.append((pointer, head))  # 현재 노드와 head 상태 저장
            if pointer.prev:
                pointer.prev.next = pointer.next
            if pointer.next:
                pointer.next.prev = pointer.prev
            # head가 삭제되는 경우 처리
            if pointer == head:
                head = pointer.next
            # 다음 노드로 이동
            pointer = pointer.next if pointer.next else pointer.prev
        elif command[0] == "Z":  # 복구
            restore_node, prev_head = stack.pop()
            if restore_node.prev:
                restore_node.prev.next = restore_node
            if restore_node.next:
                restore_node.next.prev = restore_node
            # head 복구 처리
            if not restore_node.prev:
                head = restore_node

    # 결과 생성
    result = ['X'] * n
    current = head
    while current:
        result[current.value] = 'O'
        current = current.next

    return ''.join(result)