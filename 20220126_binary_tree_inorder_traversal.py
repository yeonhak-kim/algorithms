# Binary Tree Inorder Traversal (leetcode)

# Recursive Method

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node:Optional[TreeNode], traversal:List[int]):
            # base case
            if not node:
                return
            # reading inorder: left -> read -> right
            inorder(node.left, traversal)
            traversal.append(node.val)
            inorder(node.right, traversal)
        
        result = []
        inorder(root, result)
        return result