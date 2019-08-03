#Hunter Waite
#CPE 202-13 Irene Humer

from stack_array import Stack
import operator
# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens
    are space separated.  Tokens are either operators + - * / ** << and >> or numbers
    Returns the result of the expression evaluation.
    Raises an PostfixFormatException if the input is not well-formed"""
    #deals with all the basic set up variables
    stack = Stack(30)
    if len(input_str) == 0:
        raise PostfixFormatException('Insufficient operands')
    input = input_str.split()
    if len(input) == 1 and input[0] in '0123456789':
        return float(input[0])
    #dictionary for all the operator types
    operators = {'+' : operator.add,
                 '-' : operator.sub,
                 '*' : operator.mul,
                 '/' : operator.truediv,
                 '**': operator.pow,
                 '<<': operator.lshift,
                 '>>': operator.rshift}
    #loops through all of the inputs to test
    for char in input:
        #checks for Invald Characters in the given expression
        for c in char:
            if c not in '1234567890+-*/<>.':
                raise PostfixFormatException('Invalid token')
        #pushes a number onto the stack
        if char[0] in '1234567890':
            stack.push(char)
        #performs an operation if it isn't a number
        elif char in operators:
            #this test to see whether or not there are enough items
            #in the stack to perform the operation, raises an error if
            #there is not
            try:
                temp1 = stack.pop()
                temp2 = stack.pop()
            except IndexError:
                raise PostfixFormatException('Insufficient operands')
            #checks to make sure the bitwise operators are only using
            #integers no floats, if it uses floats raises an error
            #otherwise proceeds as normal
            if char != '<<' and char != '>>':
                 if char == '/' and float(temp1) == 0:
                    raise ValueError
                 else:
                    stack.push(operators[char](float(temp2),float(temp1)))
            else:
                if '.' in str(temp1) or '.' in str(temp2):
                    raise PostfixFormatException('Illegal bit shift operand')
                else:
                    stack.push(operators[char](int(temp2),int(temp1)))
    #if the final size of the stack is greater than 1 that means
    #that there were too many operands for the expression
    if stack.size() > 1:
        raise PostfixFormatException('Too many operands')
    return stack.peek()
def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are
    space separated.  Tokens are either operators + - * / ** << and >> parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    RPNExpr = []
    stack =  Stack(30)
    input = input_str.split()
    #dictionary for the operators and their precedence,
    #where 0 is the lowest and 3 is the highest
    operators = {'+' : 0,
                 '-' : 0,
                 '*' : 1,
                 '/' : 1,
                 '**': 2,
                 '<<': 3,
                 '>>': 3}
    #loops thorugh the input string from left to right
    for char in input:
        #if the character is a number then append it to the final expression
        if char[0] in '1234567890':
            RPNExpr.append(char)
        #if the character is an open parentheses then push it to the stack
        elif char == '(':
            stack.push(char)
        #if the character is a closing parenthesis then loop throguh the
        #the stack and add everything in it until you find a closing bracket
        elif char == ')':
            if stack.size() != 0:
                while stack.peek() != '(':
                    RPNExpr.append(stack.pop())
                stack.pop()
        #handles the operators found in the input string
        else:
            #makes sure the stack is not empty
            if stack.size() != 0:
                #loops through the stack making sure the correct operators are
                #put in their correct order
                while stack.size() != 0 and stack.peek() in operators:
                    opr = stack.peek()
                    if char != '**' and operators[char] <= operators[opr] or char == '**' and operators[char] < operators[opr]:
                        RPNExpr.append(stack.pop())
                    #if the character doesn't meet the conditions then break out
                    #and push it to the stack
                    else:
                        break
            stack.push(char)
    #pushes the rest of the stack into the final expression then joins it
    #together and returns it
    for x in range(stack.size()):
        RPNExpr.append(stack.pop())
    return(' '.join(RPNExpr))
def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are
    space separated.  Tokens are either operators + - * / ** << and >> parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    stack =  Stack(30)
    input = input_str.split()
    input.reverse()
    operators = ['+','-','*','/','**','<<','>>']
    for char in input:
        if char[0] in '0123456789':
            stack.push(char)
        else:
            o1 = stack.pop()
            o2 = stack.pop()
            string = o1 +' '+ o2 +' '+ char
            stack.push(string)
    return(stack.pop())
#postfix_eval('5 1 2 + 4 << + 3 -')
#infix_to_postfix('3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3')
#prefix_to_postfix(' * - 3 / 2 1 - / 4 5 6 ')
