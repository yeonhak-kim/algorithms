# binary search tree post-order traversal implementation
def postorder(node):
    if not node:
        return
    
    # left visit
    left_visit = postorder(node.left)

    # right visit
    right_visit = postorder(node.right)

    #################
    ### VISIT     ###
    ### OPERATION ###
    #################

    # done with recent visits
    return
    
