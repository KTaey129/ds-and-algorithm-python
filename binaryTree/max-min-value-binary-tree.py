from collections import deque

def largest_node_binary_tree(root):

  if not root:
    return float('-inf')
    
  queue = deque([root])
  max_node = 0

  while queue:
  
    curr_node = queue.popleft()
  
    if curr_node.left:
      queue.append(curr_node.left)
    
    if curr_node.right:
      queue.append(curr_node.right)
    
    if curr_node.val > max_node:
      max_node = curr_node.val
  return max_node

# Recursive
def findMax(root):
  # Base case
  if (root == None):
    return float('-inf')

  # Return maximum of 3 values:
  # 1) Root's data 2) MAx in Left Subtree 3) Max in right subtree
  res = root.data
  lres = findMax(root.left)
  rres = findMax(root.right)
  return max(res, lres, rres)
