# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val  # Found the k-th smallest

        root = root.right  

    raise ValueError("k is out of range")  # Instead of returning -1

def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left  # Go as left as possible

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val  # Found the k-th smallest element

            root = root.right  # Move to the right subtree

        return -1  # This case should never be reached if k is valid
