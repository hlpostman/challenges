thing about how adding a^x+1 v a^x-1
# Closest Integer With Same Weight

The "weight" of an integer is the number of set bits in its binary representation.  Weight is only defined for unsigned integers.  For an integer *n* with weight *w*, the "closest" integer with the same weight, call it *c*, is the integer with weight *w* that minimizes |*n*-*c*| where *c* != *n*. An unsigned integer that has all bits 1's or all bits 0's has no closest integer with same weight, because for an unsigned *b*-bit integer, only one number can be represented by having all *b* bits set (namely, 2\*\*(*b*-1)), and only one number can be represented by having all *b* bits unset (namely, zero).  However, outside of the two aforementioned cases, every unsigned integer *n* is guaranteed to have a closest integer *c* of the same weight.  Furthermore, it is guaranteed that the solution set is of size one, that is, there is only one unsigned integer *c* for a given valid *n* such that *c* and *n* have the same weight and |*n*-*c*| is minimized.

[closest_int_with_same_weight](https://github.com/hlpostman/challenges/blob/master/closest_int_with_same_weight/closest_int_with_same_weight.py) takes a 64-bit unsigned integer and returns the closest integer with the same weight as defined above.  The run time is linear with respect to the place of the least significant bit adjacent to an unset bit - however, it has a constant upper limit of at most int_size, an optional argument that defaults to 64 and accepts the smaller alternative integer widths 4, 8, 16, and 32.  Space complexity is constant - nothing is stored.

The algorithm is to iterate over the bits in the integer passed, considering adjacent pairs.  We want to find a pair where on bit is set, and the other is not.  We want to find the least significant of these pairs, so we search through the bits of the integer passed starting by looking at bits 0 and 1, and then at bits 1 and 2 and so forth.  

Address the following:
- why adjacent
- why the order doesn't matter
- why least significant pair
