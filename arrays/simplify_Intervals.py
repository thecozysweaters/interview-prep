'''
Given an array of instances of the Interval class, merge all of the Intervals whose ranges overlap.

Example:

[(1, 3), (2, 6), (10, 15), (4, 8), (12, 19)] => [(1, 8), (10, 19)]
[(1, 3), (2, 6), (4, 8), (10, 15), (12, 19)]
'''

class Interval(object):
    def __init__(self, start = 0, end = 0):
        self.start = start
        self.end = end

def simplifyIntervals(A):
    A.sort(key = lambda x: x.start)  
    i = 0
    while i < len(A) - 1:
        # Look at the next Interval and try to merge.
        currentInterval = A[i]
        nextInterval = A[i + 1]
        if nextInterval.start - currentInterval.end <= 1: 
            A[i + 1] = Interval(currentInterval.start, nextInterval.end)
            A = A[:i] + A[i+1:]
        else: i += 1
    return A