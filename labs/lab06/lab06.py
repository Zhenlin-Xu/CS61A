from numpy import insert


def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurence of entry and then returns lst.
    
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    idx_insert = []
    for idx, ele in enumerate(lst):
        if ele == entry:
            idx_insert.append(idx)
    for num, idx in enumerate(idx_insert):
        lst.insert(num+idx+1, elem)
    return lst

def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it multiplied by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for ele in it:
        yield multiplier * ele

def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.
    
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    def helper(n):
        if n == 1:
            return 1
        elif n % 2 == 0:
            return n / 2
        else:
            return 3 * n + 1
    
    seq = [n]
    while n != 1:
        n = helper(n)
        seq.append(int(n))
    yield from seq