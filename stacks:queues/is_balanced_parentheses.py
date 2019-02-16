def isBalancedParentheses(text):
    '''
    Given a string, text, return True if the string's parentheses are balanced and False if they are unbalanced.

    ex. 
    "()()()(((())))" => True
    "(()))" => False
    "" => True
    '''

    stack = []
    tokens = list(text)
    while len(tokens) > 0:
        char = tokens.pop(0)
        # If you encounter an opening paranthese, "(", push it onto the stack.
        if (char == "("): stack.append(char)
        elif (char == ")"):
            if len(stack) == 0: return False
            else: stack.pop()
    
    return len(stack) == 0
