def reverseLinkedListInRange(head, start, end):
    '''
    Given the head node of a Linked List and a start and end index, reverse the order of the nodes between the start and end
    indicies.

    Example:
    head -> 1 -> 2 -> 3 -> 4 -> 5, start = 2, end = 4. Result => head -> 1 -> 4 -> 3 -> 2 -> 5
    '''
    currNode = head
    i = 1
    beforeNodes = []
    inNodes = []
    afterNodes = []

    while i <= end + 1
        if i < start: beforeNodes.append(currNode)
        elif i in range(start,end + 1): inNodes.append(currNode)
        else: afterNodes.append(currNode)
        i += 1

    for i in range(len(inNodes) - 1, -1, -1):
        if i == 0: inNodes[i].next = afterNodes[0]
        else: inNodes[i].next = inNodes[i -1]

    beforeNodes[-1].next = inNodes[-1]
    return head