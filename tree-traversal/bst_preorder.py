# binary search tree pre-order traversal implementation
def preorder(node):
    if not node:
        return

    #################
    ### VISIT     ###
    ### OPERATION ###
    #################
    
    # left visit
    left_visit = preorder(node.left)

    # right visit
    right_visit = preorder(node.right)


    # done with recent visits
    return
    
