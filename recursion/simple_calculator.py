def simpleCalculator(expression):
    '''
    Given an input expression as a string, return the mathematical result as an integer.
    Remember the order of operations: multiply, divide, add, subtract.

    ex. "13+8*2" => 29
    '''

    expression = list(expression)

    for i in range(len(expression)):
        if expression[i] == "+": return simpleCalculator(expression[:i]) + simpleCalculator(expression[i+1:])
        elif expression[i] == "-": return simpleCalculator(expression[:i]) - simpleCalculator(expression[i+1:])
    for i in range(len(expression)):
        if expression[i] == "*": return simpleCalculator(expression[:i]) * simpleCalculator(expression[i+1:])
        elif expression[i] == "/": return simpleCalculator(expression[:i]) / simpleCalculator(expression[i+1:])
    
    return int("".join(expression))