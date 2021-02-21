# rectangle_intersection.py
# 24 July 2018

def rectangle_intersection(rect_A_lower_left, rect_A_upper_right, rect_B_lower_left, rect_B_upper_right):
    """Takes four 2-tuples uniquely determining two rectangles in the plane with edges parallel to axes, detects whether or not the two rectangles intersect, if so returns two 2-tuples determining the rectangle made by the intersection.  Intersecting boundaries are considered an intersection, e.g. if rectangles A and B share a corner, that point is considered the intersection.

        Args: Each argument is a tuple of 2 non-negative integers or floats, the first entry being the x coordinate and the second being the y coordinate, specifying the given corner of the given rectangle

            rect_A_lower_left_coord: lower left corner of rectangle A
            rect_A_upper_right_coord: upper right corner of rectangle A
            rect_B_lower_left_coord: lower left corner of rectangle B
            rect_B_upper_right_coord: upper right corner of rectangle B

        Returns: List of two tuples, each tuple containing exactly two integers
            If A and B intersect: first tuple the lower left corner of the rectangle created by the intersection of A and B, second tuple the upper right corner
            If A and B do not intersect: [(float('inf'),float('inf')),(float('inf'),float('inf'))]
        Raises:
            TypeError: Expecting four tuples, each containing exactly two entries both of which are integers.
    """
    # Error handling
    arguments = [rect_A_lower_left, rect_A_upper_right, rect_B_lower_left, rect_B_upper_right]
    for argument in arguments:
        # Non-tuple argument
        if not isinstance(argument, tuple):
            raise TypeError("Expecting tuple. Given %s."% type(argument))
        else:
            # Wrong number of elements in tuple
            if len(argument) != 2:
                raise TypeError("Expecting tuple of length 2. Given tuple of length %d."%len(argument))
            for elt in argument:
                # Non-integer, non-float type in tuple
                if not (isinstance(elt, float) or isinstance(elt, int)) :
                    raise TypeError("Expecting tuple of non-negative integers or floats. Given tuple containing %s."% type(elt))
                # Negative values in tuples
                if elt < 0:
                    raise ValueError("Expecting non-negative tuple elements. Given tuple containing %d." %elt)
    # End error handling

    def is_rectangle_intersection(rect_A_lower_left, rect_A_upper_right, rect_B_lower_left, rect_B_upper_right):
        """Takes four 2-tuples each containing two non-negative integers or floats uniquely determining two rectangles in the plane with edges parallel to axes, detects whether or not the two rectangles intersect, if so returns True, else False.  Intersecting boundaries are considered an intersection, e.g. if rectangles A and B share a corner, that point is considered the intersection.
        """
        A_width = rect_A_upper_right[0] - rect_A_lower_left[0]
        A_height = rect_A_upper_right[1] - rect_A_lower_left[1]
        B_width = rect_B_upper_right[0] - rect_B_lower_left[0]
        B_height = rect_B_upper_right[1] - rect_B_lower_left[1]

        return (rect_A_lower_left[0] <= rect_B_lower_left[0] + B_width and rect_A_lower_left[0] + A_width >= rect_B_lower_left[0] and rect_A_lower_left[1] <= rect_B_lower_left[1] + B_height and rect_A_lower_left[1] + A_height >= rect_B_lower_left[1])

    if not is_rectangle_intersection(rect_A_lower_left, rect_A_upper_right, rect_B_lower_left, rect_B_upper_right):
        return [(float('inf'),float('inf')),(float('inf'),float('inf'))]

    rect_R_lower_left_x = max(rect_A_lower_left[0], rect_B_lower_left[0])
    rect_R_lower_left_y = max(rect_A_lower_left[1], rect_B_lower_left[1])
    rect_R_upper_right_x = min(rect_A_upper_right[0], rect_B_upper_right[0])
    rect_R_upper_right_y = min(rect_A_upper_right[1], rect_B_upper_right[1])

    return [(rect_R_lower_left_x, rect_R_lower_left_y), (rect_R_upper_right_x, rect_R_upper_right_y)]
