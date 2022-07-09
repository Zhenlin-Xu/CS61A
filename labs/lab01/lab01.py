def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    for idx in range(k):
        result *= n-idx
    return result


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    result = 0
    if y < 10:
        return y
    else:
        while y > 9:
            left = y // 10
            right = y % 10
            result += right
            y = left
        return result + y

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return False
    elif n == 88:
        return True

    digits = []
    while n > 9 :
        left = n // 10
        right = n % 10
        digits.append(right)
        n = left
    digits.append(n)
    for idx in range(len(digits)-1) :
        if digits[idx] == 8 and digits[idx+1] == 8 :
            return True
    return False
