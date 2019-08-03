def bears(n):
    """A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
    bears."""
    if n == 42:
        return True
    if n < 42:
        return False
    if (n % 2) == 0:
        if bears(int(n/2)):
            return True
    if (n % 3) == 0 or (n % 4) == 0 and (n-((n%10)*(int((n%100)/10)))):
        num1 = int((n%100)/10)
        num2 = n%10
        if num1 and num2:
            return bears(n-int(num1*num2))
    if (n % 5) == 0:
        if bears(n-42):
            return True
    return False

    
