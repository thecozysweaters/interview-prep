def merge(A, B):
  C = []
  while len(A) > 0 and len(B) > 0:
    if A[0] <= B[0]:
      C.append(A.pop(0))
    else:
      C.append(B.pop(0))
  
  if len(A) > 0: C += A
  elif len(B) > 0: C += B
  return C    
    
def threeWayMergeSort(A):
    # base case: A is empty or only one element so it's already sorted
    n = len(A)
    if n < 2: return A

    mid1 = int(n / 3)
    mid2 = 2 * int(n/ 3)

    return merge(merge(A[:mid1], A[mid1:mid2]), A[mid2:])