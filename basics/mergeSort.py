def merge(A, B):
    '''
    Given two sorted arrays, A and B, return a single sorted array of all the elements in both A and B
    '''
    C = []
    while len(A) > 0 and len(B) > 0:
        if A[0] <= B[0]:
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
    
    if len(A) > 0: C = C + A
    if len(B) > 0: C = C + B

    return C

def mergeSort(A):
    '''
    Given an array A, return it sorted.
    '''
    # if A is empty or only one element, it is already sorted.
    if len(A) < 2: return A
    # merge the two halves of A.
    mid = int(len(A) / 2)
    return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))
