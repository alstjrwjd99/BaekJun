import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value, x, y):
        self.value = value  # 노드 번호
        self.x = x          # x 좌표
        self.y = y          # y 좌표
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.answer = [[], []] 
    
    def push(self, node):
        if self.root is None: 
            self.root = node
            return
        current = self.root
        while True: 
            if node.x < current.x:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right

    def preOrder(self, node):
        if node is not None:
            self.answer[0].append(node.value)  # 현재 노드 방문
            self.preOrder(node.left)
            self.preOrder(node.right)

    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            self.answer[1].append(node.value)  # 현재 노드 방문

    def getAnswer(self):
        self.preOrder(self.root)  # 전위 순회
        self.postOrder(self.root)  # 후위 순회
        return self.answer

def solution(nodeinfo):
    sorted_nodes = sorted([(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)], key=lambda x: (-x[2], x[1]))
    nodes = [Node(num, x, y) for num, x, y in sorted_nodes]
    
    tree = Tree()
    for node in nodes:
        tree.push(node)
    
    return tree.getAnswer()