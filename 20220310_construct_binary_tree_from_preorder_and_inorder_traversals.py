# Construct Binary Tree from Preorder and Inorder Traversals (leetcode)


# preorder and inorder lists
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(in_left = 0, in_right = len(preorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None
            
            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion 
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root
        
        inorder = sorted(preorder)
        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper()


# left_bound and right_bound

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def traverse(left_bound:float, right_bound:float) -> Optional[TreeNode]:
            nonlocal idx
            nonlocal N
            if idx == N:
                return None
            
            node_val = preorder[idx]
            
            if not (left_bound <= node_val <= right_bound):
                return None
            
            idx += 1
            node = TreeNode(node_val)
            node.left = traverse(left_bound, node_val - 1)
            node.right = traverse(node_val + 1, right_bound)
            
            return node
        
        N = len(preorder)
        idx = 0
        return traverse(float('-inf'), float('inf'))