def findOddOneOut(A):
    '''
    Given an array, A, find the element that appears an odd number of times.
    [0, 0, 1, 1, 2, 3, 3, 4, 4] => 2
    [0, 1, 0, 1, 2, 3, 3] => 2
    '''

    answer = 0
    for i in A:
        answer ^= i

    return answer