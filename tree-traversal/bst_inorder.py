# binary search tree in-order traversal implementation
def inorder(node):
    if not node:
        return

    # left visit
    left_visit = inorder(node.left)

    #################
    ### VISIT     ###
    ### OPERATION ###
    #################

    # right visit
    right_visit = inorder(node.right)

    # done with recent visits
    return

