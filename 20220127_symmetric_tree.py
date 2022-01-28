# Symmetric Tree (leetcode)

# Tree Traversal (Recursive)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(left:Optional[TreeNode], right:Optional[TreeNode]) -> bool:
            # base case 0 : left and right both NULL
            if not left and not right: return True
            
            # base case 1 : if either one is NULL then mismatch found
            if not left or not right: return False
            
            # base case 2 : left and right values checks
            if left.val != right.val: return False
            
            # traverse through the tree
            validity1 = compare(left.right, right.left)
            validity2 = compare(left.left, right.right)
            
            # validation check for left-subtree and right subtree
            return validity1 and validity2
        
        return compare(root.left, root.right)