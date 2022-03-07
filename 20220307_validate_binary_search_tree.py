# Validate Binary Search Tree

# left bound and right bound
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validity_check(node:Optional[TreeNode], left_bound: float, right_bound: float) -> bool:
            if not node:
                return True
            
            if node.val <= left_bound:
                return False
            
            if node.val >= right_bound:
                return  False
            
            return validity_check(node.left, left_bound, node.val) and validity_check(node.right, node.val, right_bound)
        
        return validity_check(root, float('-inf'), float('inf'))
            
            
# inorder traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node:Optional[TreeNode]) -> bool:
            nonlocal prev
            if not node:
                return True
            
            if not inorder(node.left):
                return False
            
            if node.val <= prev:
                return False
            
            prev = node.val
            
            return inorder(node.right)
        
        prev = float("-inf")
        return inorder(root)
            
            
            
            
                  
            
            
