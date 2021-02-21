# increment_arbitrary_precision_integer.py
# 26 July 2018

def increment_arbitrary_precision_integer(A):
    """Returns a new array that increments the integer represented by the array passed.

        Args: A, an array of non-negative integers representing a non-negative integer in base 10, e.g. A = [1,5,0] means A represents the number 150.  Each entry is an element of range(0,10).

        Returns: An array of non-negative integers representing the base 10 integer one greater than the non-negative integer represented in the array passed.  Each entry is an element of range(0,10).  Note the size of the array may be equal to or one greater than the size of the array passed.  Returns an empty array if A is empty.

        Raises:
            TypeError: Expecting an array of  integers
            ValueError: Expecting element of range(0,10)
    """
    # Error handling
    # Check for array
    if not isinstance(A, list): # Raise error for empty non-list collection types rather than return them in len(A) == 0 check later
        raise TypeError("Expecting array of integers. Received object of type %s." %type(A))
    # Check elements of array
    for element in A:
        if not isinstance(element, int):
            raise TypeError("Expecting array of integers. Received array containing type %s." %type(element))
        elif element not in range(10):
            raise ValueError("Expecting array elements in range(0,10). Received %d." %element)
    # End error handling

    A_incremented = A
    if len(A) == 0:
        return A_incremented
    # No carry (simple case; last digit < 9)
    if A[-1] < 9:
        A_incremented[-1] += 1
        return A_incremented

    # Carry case (if the last digit is 9)
    i = -1
    while abs(i) <= len(A) and A[i] == 9: # Fill in 0's
        A_incremented[i] = 0
        i -= 1
    if abs(i) <= len(A): # Increment
        A_incremented[i] += 1
        return A_incremented
    else: # Increment by adding place (Every digit in A was 9, e.g. [9,9,9].  Add ten's place)
        return [1] + A_incremented
