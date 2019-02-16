def findShift(A):
    '''
    Given a shift sorted array, A (e.g. [4, 5, 0, 1, 2, 3]), return the amount that the array is shifted by.
    '''
    i = 0
    j = len(A) - 1

    if (A[i] < A[j]): return 0
    else:
        min_index = 0
        min_so_far = A[min_index]
        for i in range(len(A)):
            if A[i] < min_so_far: 
                min_so_far = A[i]
                min_index = i
    return min_index

def binarySearch(A, target, start=0):
    '''
    Given a sorted array, A, and a target value, return the index at which the target value occurs and -1 if the target
    does not appear in A.
    '''
    if len(A) == 0: return -1
    
    midpoint = int(len(A) / 2)
    if A[midpoint] == target: return midpoint
    elif A[midpoint] > target: return binarySearch(A[:midpoint], target, start)
    else: return midpoint + binarySearch(A[midpoint:], target, start + midpoint + 1)


def searchShiftSortedArray(A, target):
    '''
    Given a shift sorted array, A (e.g. [4, 5, 0, 1, 2, 3]), and a target value, return the index at which the target
    value occurs in A and -1 if the target value does not appear.
    '''

    # First, find the amount that A is shifted by. This will be our pivot position.
    pivot = findShift(A)
    # binary search the two halves of the array:
    result = binarySearch(A[:pivot], target, 0)
    if result == -1:
      return binarySearch(A[pivot:], target, pivot)
    else: 
      return result