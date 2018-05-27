# swap_bits.py
# 27 May 2018

def swap_bits(n, i, j):
    """Takes an integer and two bit places, and returns the integer with
    specified bits swapped.

    Args:
        n: any number that is an integer in Python
        i, j: both non-negative integers less than 64 specifying which bits to
        swap

    Returns:
        the integer n with the ith and jth bits swapped
        e.g. swap_bits(5,0,1) => 6

    Raises:
        ValueError: i and/or j is negative
        TypeError: n, i, and/or j is not an integer
    """
    # A swap is only necessary if the ith and jth bits are different. If they
    # differ, return n with the ith and jth bits flipped, else simply n
    if (n>>i)&1 != (n>>j)&1:
        bit_mask = (1<<i) | (1<<j)
        return(n ^ bit_mask)
    return(n)
