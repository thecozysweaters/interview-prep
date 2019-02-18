def LCAForBST(root, e1, e2):
    '''
    Given the root node of a BST and two elements, e1 and e2, return the value of the lowest common ancestor of the two nodes.
    '''

    '''
    Observation: the lowest common ancestor of two nodes occurs when the current node is greater than or equal to one
    node and less than or equal to the other node.
    '''

    small = min(e1, e2)
    big = max(e1, e2)

    if root.val >= small and root.val <= big: return root.val
    elif root.val > small and root.val > big: return LCAForBST(root.left, e1, e2)
    else: return LCAForBST(root.right, e1, e2)