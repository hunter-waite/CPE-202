
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    remainder = num%b
    if remainder >= 10:
        remainder = to_hex(remainder)
    newNum = num//b
    
    if newNum == 0:
        return remainder
    else:
        return str(convert(newNum,b)) + str(remainder)
def to_hex(num):
    '''Brute force converts decimal numbers to their hex coefficients'''
    if num == 10:return 'A'
    elif num == 11:return 'B'
    elif num == 12:return 'C'
    elif num == 13:return 'D'
    elif num == 14:return 'E'
    elif num == 15:return 'F'
