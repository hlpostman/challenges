# closest_int_with_same_weight.py
# 16 June 2018

def closest_int_with_same_weight(n):
    """ Returns the nearest integer to n that has the same weight (number of set bits) as n, where "nearest" means the that the absolute value of the difference of n and the integer returned is as small as possible. Integer returned is guaranteed to be different than n.

    Args:
        n: an unsigned 64-bit integer

    Returns:
        an unsigned 64-bit integer

    Raises:
        ValueError: n is signed or does not fit in 64 bits
        TypeError: n is not an integer
    """
    INT_SIZE = 64
    for i in range(INT_SIZE-1):
        # Find the lsb that has an unset neighbor
        if (n >> i)&1 != (n >> (i+1))&1:
            # Swap bits
            n^= (1 << i) | (1 << (i+1))
            return n
    raise ValueError('All 0\'s or 1\'s. No 64-bit integer with the same weight exists.')
