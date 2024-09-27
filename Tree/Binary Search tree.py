#       5
#    1    8
#  -1 3  7 9
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.val)
  
A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

# Recursive In Order Traversal (DFS) Time: O(n), Space: O(n)
def in_order(node):
  if not node:
    return

  in_order(node.left)
  print(node)
  in_order(node.right)

in_order(A2)

# Remove this line as it's redundant and will print None
# print(in_order(A2))

# Time: O(log n), Space: O(log n)
def search_bst(node, target):
  if not node:
    return False

  if node.val == target:
    return True

  if target < node.val: return search_bst(node.left, target)
  else: return search_bst(node.right, target)

print(search_bst(A2, -1))  # Add print statement to see the result