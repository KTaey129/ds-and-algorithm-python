# LeetCode 236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_iterative:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        parent = {root: None}

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                parent[node.left] = node

            if node.right:
                queue.append(node.right)
                parent[node.right] = node

            if p in parent and q in parent:
                break

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q:
            if q in ancestors:
                return q
            q = parent[q]

        pointer1, pointer2 = p, q

        # Move both pointers up unitl they meet
        while pointer1 != pointer2:
            pointer1 = parent[pointer1] if pointer1 else q
            pointer2 = parent[pointer2] if pointer2 else p

        return pointer1

  class Solution_recursive:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None: return root
        if left != None: return left
        return right
