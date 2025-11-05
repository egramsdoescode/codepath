class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


from collections import deque


def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")

root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")

root.right.right = TreeNode("Gala")
root.right.left = TreeNode("Crab")

print("--- Problem 1 ---")
print_tree(root)


print("\n--- Problem 2 ---")


def calculate_yield(root):
    if not root:
        return
    if root.val == "+":
        return root.left.val + root.right.val
    if root.val == "-":
        return root.left.val - root.right.val
    if root.val == "*":
        return root.left.val * root.right.val
    if root.val == "/":
        return root.left.val / root.right.val


"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))

print("\n--- Problem 3 ---")


def right_vine(root, lst):
    if not root.right.val:
        lst.append(root.val)
        return lst
    list.append(root.right.val)
    return right_vine(root.right, lst)


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""

ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1, []))
print(right_vine(ivy2, []))
