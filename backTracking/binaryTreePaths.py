# https://leetcode.com/problems/binary-tree-paths/description/?envType=problem-list-v2&envId=backtracking

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def backtrack(node, path):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                backtrack(node.left, path)
                backtrack(node.right, path)
                
            path.pop()

        result = []
        backtrack(root, [])
        return result
