# https://leetcode.com/problems/delete-node-in-a-bst/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # Key found
            if not root.left:  # No left child
                return root.right
            elif not root.right:  # No right child
                return root.left
            else:  # Two children
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)

        return root

class Solution_iterative:
    def deleteNode(self, root, key):
        if not root:
            return None

        parent = None  # Keep track of the parent node
        curr = root    # Current node we're examining

        # 1. Search for the node to delete (iteratively)
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        # 2. Key not found
        if not curr:
            return root

        # 3. Key found!  Handle deletion cases
        if not curr.left:  # Case 1: No left child
            if not parent:  # Deleting the root
                return curr.right
            elif curr == parent.left:
                parent.left = curr.right
            else:
                parent.right = curr.right
            return root  # Important: Return the root (might be unchanged)

        elif not curr.right:  # Case 2: No right child
            if not parent:  # Deleting the root
                return curr.left
            elif curr == parent.left:
                parent.left = curr.left
            else:
                parent.right = curr.left
            return root

        else:  # Case 3: Two children
            # Find inorder successor (iteratively)
            successor_parent = curr
            successor = curr.right
            while successor.left:
                successor_parent = successor
                successor = successor.left

            curr.val = successor.val  # Replace with successor's value

            # Delete the successor (which is now either a leaf or has only a right child)
            if successor == successor_parent.left:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

            return root
