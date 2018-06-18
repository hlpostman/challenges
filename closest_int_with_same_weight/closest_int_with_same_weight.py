# closest_int_with_same_weight.py
# 17 June 2018

def closest_int_with_same_weight(n, int_size=64):
    """ Returns the nearest integer to n that has the same weight (number of set bits) as n, where "nearest" means the that the absolute value of the difference of n and the integer returned is as small as possible. Integer returned is guaranteed to be different than n.

    Args:
        n: an unsigned 64-bit integer
        int_size: an optional argument specifying the size of the integer passed.  Default is 64.  Other valid values are 4, 8, 16, and 32.

    Returns:
        an unsigned 64-bit integer

    Raises:
        TypeError: n is not an integer and/or int_size is not an integer
        ValueError: 1) int_size is not a valid integer size
                    2) n is larger than the integer size passed
                    3) n is all 0's or all 1's.  No other integer of the same size with the same weight exists
    """
    # Error handling
    if not isinstance(int_size, int):
        raise TypeError('Invalid type passed for int_size argument.  The int_size must be an integer.')
    if int_size not in (4,8,16,32,64):
        raise ValueError('Invalid integer size.  Valid integer sizes are 4, 8, 16, 32, and 64.')
    if n > 2**int_size:
        raise ValueError('Integer passed is too large for integer size.  Integer size is an optional arguement defaulting to 64.  Other valid values are 4, 8, 16, and 32.  Integer passed: %d.  Integer size passed: %d.'%(n, int_size))

    # Algorithm
    for i in range(int_size-1):
        # Find the lsb that has an unset neighbor
        if (n >> i)&1 != (n >> (i+1))&1:
            # Swap bits
            n^= (1 << i) | (1 << (i+1))
            return n

    # Error handling
    raise ValueError('All 0\'s or 1\'s. No %d-bit integer with the same weight exists.'%int_size)
