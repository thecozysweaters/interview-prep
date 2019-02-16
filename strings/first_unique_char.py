def firstUniqueChar(str):
    '''
    Given a string, str, return the first letter that appears only once.
    '''

    lettersSeen = {}
    for c in str:
        if c in lettersSeen: lettersSeen[c] += 1
        else: lettersSeen[c] = 1
    
    for c in str:
        if lettersSeen[c] == 1: return c
    
    return -1
