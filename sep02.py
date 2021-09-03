# Leetcode Daily Challenge
# September 02: Unique Binary Search Trees 2

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Helper function
        def generateAllSets(start, end) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            
            all_sets = []
            for i in range(start, end + 1):
                # all cases for left subtrees
                left_subtrees = generateAllSets(start, i - 1)
                # all cases for right subtrees
                right_subtrees = generateAllSets(i + 1, end)
                
                for j in range(len(left_subtrees)):
                    for k in range(len(right_subtrees)):
                        tree = TreeNode(i, left_subtrees[j], right_subtrees[k])
                        all_sets.append(tree)
            
            return all_sets
        
        return generateAllSets(1, n)