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

def right_vine(root):
    result = []

    if not root:
        return result
    
    if not root.right:
        return [root.val] 

    def helper(root):
        nonlocal result
        if not root:
            return
        result.append(root.val)         
        helper(root.right)

    helper(root)
    return result



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

print(right_vine(ivy1))
print(right_vine(ivy2))

print("\n--- Problem 4 ---")
def right_vine_iter(root):
    if not root:
        return []

    if not root.right:
        return [root.val]

    result = []
    
    curr = root
    while curr:
        result.append(curr.val)
        curr = curr.right

    return result

print(right_vine_iter(ivy1))
print(right_vine_iter(ivy2))

print("\n--- Problem 5 ---")

def count_leaves(root):
    count = 0
    if not root:
        return count

    if not root.right:
        return count + 1

    def helper(root):
        nonlocal count
        if not root:
            return
        count += 1 
        helper(root.right) 

    helper(root)
    return count


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))

print("\n--- Problem 6 ---")

def survey_tree(root):
    result = [] 
    if not root:
        return result 

    def helper(root):
        nonlocal result
        if not root:
            return
        helper(root.left)
        helper(root.right)
        result.append(root.val)
        
    helper(root)

    return result


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))


print("\n--- Problem 7 ---")

def harvest_berries(root, threshold):
    sum = 0 
    
    def helper(root, threshold):
        nonlocal sum
        if not root:
            return

        if root.val > threshold:
            sum += root.val
        
        helper(root.left, threshold)
        helper(root.right, threshold)


    helper(root, threshold)
    return sum

"""
       4
     /   \
   10     6
  /  \     \
 5    8    20
"""
bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

print(harvest_berries(bush, 6))
print(harvest_berries(bush, 30))


"""
         Rose
        /    \
       /      \
     Lily     Daisy
    /    \        \
Orchid  Lilac    Dahlia
"""

print("\n--- Problem 8 ---")
def find_flower(root, flower):
    found = False  
    
    def helper(root, flower):
        nonlocal found
        if not root:
            return
        if root.val == flower:
            found = True

        helper(root.left, flower)
        helper(root.right, flower)
    
    helper(root, flower)
    return found

flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))
print(find_flower(flower_field, "Hibiscus"))











