# Maximum Depth of Binary Tree (leetcode)


# Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_height(node:Optional[TreeNode]) -> int:
            # base case : reached end
            if not node: return 0
            
            # get heights for left and right subtrees
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # add 1 height
            return max(left_height, right_height) + 1
        
        return get_height(root)