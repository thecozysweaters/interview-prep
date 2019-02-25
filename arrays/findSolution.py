def findSolution(A):
    '''
    Given an array of non-negative integers. You are initally positioned at the 0 index. Each element's value represents 
    the length of the "jump" you can make (ie how many indecies you can move from that index). Return True if you are 
    able to travel from the first index to the last index and False otherwise.

    [3, 2, 1, 0, 4] => False
    [2, 3, 1, 0, 1] => True
    '''
    if len(A) < 2: return True
    for i in range(len(A) - 1, -1, -1):
        if (A[i] >= len(A) - 1 - i) and findSolution(A[:i]): return True
    return False
