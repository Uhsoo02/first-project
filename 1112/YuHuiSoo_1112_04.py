# 과제4: 트리 순회
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024-11-12

class TNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def preorder(n, step = 0):
    if n is not None:
        print(f"Step {step}: Visiting node {n.data} in Preorder")
        preorder(n.left, step + 1)
        preorder(n.right, step + 1)

def inorder(n, step = 0):
    if n is not None:
        inorder(n.left, step + 1)
        print(f"Step {step}: Visiting node {n.data} in Inorder")
        inorder(n.right, step + 1)

def postorder(n, step = 0):
    if n is not None:
        postorder(n.left, step + 1)
        postorder(n.right, step + 1)
        print(f"Step {step}: Visiting node {n.data} in postorder")

d = TNode('D')
e = TNode('E')
b = TNode('B', d, e)
f = TNode('F')
c = TNode('C', f)
root = TNode('A', b, c)

print("In-Order Traversal Steps:")
inorder(root)
print("\nPre-Order Traversal Step:")
preorder(root)
print("\nPost-Order Traversal Steps:")
postorder(root)