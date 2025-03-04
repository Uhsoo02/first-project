# 과제3: 
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024-11-12

class TNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

step_counter = 1

def calc_height(root):
    global step_counter

    if root is None:
        print(f"Step {step_counter:02d}: None 노드 -> 높이 0 반환")
        step_counter += 1
        return 0
    
    print(f"Step {step_counter:02d}: 노드 '{root.data}' 방문")
    step_counter += 1

    hLeft = calc_height(root.left)
    hRight = calc_height(root.right)

    height = max(hLeft, hRight) + 1
    print(f"Step {step_counter:02d}: 노드 '{root.data}'의 높이는 max({hLeft}, {hRight}) + 1 = {height}")
    step_counter += 1

    return height

d = TNode('D')
e = TNode('E')
b = TNode('B', d, e)
f = TNode('F')
c = TNode('C', f)
root = TNode('A', b, c)

print("트리의 높이 =", calc_height(root))