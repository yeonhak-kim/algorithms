# Diameter of Binary Tree (leetcode)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_height(node:Optional[TreeNode]) -> int:
            nonlocal MAX_DISTANCE
            if not node: return 0
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            MAX_DISTANCE = max(left_height + right_height, MAX_DISTANCE)
            return max(left_height, right_height) + 1
        
        MAX_DISTANCE = 0
        get_height(root)
        return MAX_DISTANCE