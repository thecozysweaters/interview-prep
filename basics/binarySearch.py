def binarySearch(A, target, start=0):
    '''
    Given a sorted array, A, and a target value, return the index in A at which the target value appears and -1 if the
    target value does not appear in A.
    '''
    # Edge case: A is empty.
    n = len(A)
    if n == 0: return -1

    mid = int(n/2)
    
    if A[mid] == target:
      # The midpoint is the target value so return the midpoint.
      return start + mid
    elif A[mid] > target:
      # The value at the midpoint is greater than the target value so binary search the array up to the midpoint.
      # Pass in the previous value of start since it hasn't changed.
      return binarySearch(A[:mid], target, start)
    else:
      # The value of the midpoint is less than the target value so binary search the array after the midpoint. The new 
      # start is the old start + midpoint + 1
      return binarySearch(A[mid + 1:], target, start + mid + 1)