def depthFirstSearch(root, target):
    if root == None: return False
    elif root.val == target: return True
    elif depthFirstSearch(root.left, target): return True
    elif depthFirstSearch(root.right, target): return True
    return False

def LCAForBT(root, e1, e2, where={}):
    '''
    Given the root node of a BT and two elements, e1 and e2, return the value of the lowest common ancestor of the two nodes.
    '''
    
    if root.val == e1: where[e1] == "here"
    elif depthFirstSearch(root.left, e1): where[e1] = "left"
    elif depthFirstSearch(root.right, e1): where[e1] = "right"
    
    if root.val == e2: where[e2] == "here"
    elif depthFirstSearch(root.left, e2): where[e2] = "left"
    elif depthFirstSearch(root.right, e2): where[e2] = "right"
    
    if where[e1] != where[e2]: return root.val
    elif where[e1] == "left": return LCAForBT(root.left, e1, e2)
    else: return LCAForBT(root.right, e1, e2)