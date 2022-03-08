# Binary Tree Level Order Traversal

# Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        current_level = deque([root])
        next_level = deque()
        level = []
        while current_level:
            level_node = current_level.popleft()
            level.append(level_node.val)
            
            if level_node.left:
                next_level.append(level_node.left)
            if level_node.right:
                next_level.append(level_node.right)
                
            if not current_level:
                current_level = next_level
                next_level = deque()
                result.append(level)
                level = []

        return result
                
                
        