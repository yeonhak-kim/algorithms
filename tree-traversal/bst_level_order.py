# binary search tree level order traversal

# recursive method
def levelorder(node):
    # retrieve number of levels
    levels = height(node) + 1

    # visit all levels
    for level in range(levels):
        level_visit(node, level)
    

# visit nodes in target level
def level_visit(node, target_level):
    if not node:
        return
    
    if target_level == 1:
        # target level reached #
        # has access to only one node at the level (currently visiting)

        #################
        ### OPERATION ###
        #################
        pass

    else:
        level_visit(node.left, target_level - 1)
        level_visit(node.right, target_level - 1)
    
    return

# compute height
def height(node):
    if not node:
        return 0

    # retrieve left height
    left_height =  height(node.left)

    # retrieve right height
    right_height = height(node.right)

    return max(left_height, right_height) + 1

#####################################################################################################
#####################################################################################################

# iterative method
from collections import deque

# visit sequentially
def levelorder_sequential(node):
    if not node:
        return

    queue = deque([node])
    while queue:
        # retrieve next node to visit
        node = queue.popleft()

        if node.left:
            # append left node
            queue.append(node.left)

        if node.right:
            # append right node
            queue.append(node.right)

# visit level by level
def levelorder(node):
    if not node:
        return
    
    current_level = deque([node])
    next_level = deque([])

    while current_level:
        node = current_level.popleft()

        #################
        ### OPERATION ###
        #################

        if node.left:
            next_level.append(node.left)

        if node.right:
            next_level.append(node.right)
        
        if not current_level:
            # done with visiting all nodes in the current level
            if next_level:
                # if there exists next level, visit from next round
                current_level = next_level
                next_level = deque([])
    
    return 