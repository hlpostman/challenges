# challenges
A pythonic tour of frameworks and algorithms

#### Dependencies

* [pytest](https://github.com/pytest-dev/pytest)
* [requests](https://github.com/requests/requests)
* [twisted](https://github.com/twisted/twisted)
* [numpy](https://github.com/numpy/numpy)
* [scipy](https://github.com/scipy/scipy)

#### Algorithms
###### Interleave

Interleave takes a stack and modifies it in place so that groups of elements that were originally in the front of the stack retain their order within the group and with respect to other "front" groups, but are interspersed with groups of elements that were originally in the back of the stack.  The groups of elements that were originally in the back of the stack have *reverse* order with respect to each other and other "back" groups.  [interleave.py](link to file in merged repo) implements the simplest version of this function. [interleave_with_optional_arguments.py](link to file in merged repo) implements a version of this function that allows for customization as described below.

* Groups: A simple example would be where groups have size 1, so there is a simple braiding that happens: `[0,1,2,3,4,5] => [0,5,1,4,2,3]`.  An example with groups of size larger than 1 - say, size 3, - would be `[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14] => [0,1,2,14,13,12,3,4,5,11,10,9,6,7,8]`.  The default group size is 1.  

* Offsetting: Interleave can also take an offset, so you can start the weave farther into the stack if you prefer.  Interleaving a stack of 10 elements with an offset of 5 would interleave just the last 5 elements: `[0,1,2,3,4,5,6,7,8,9] => [0,1,2,3,4,5,9,6,8,7]`.  The first element in an interleave stays in place, so while the 5 looks like it was part of the first few untouched elements, it was considered in the interleaving of the last 5 elements.  The default offset is 0.

The word "front" is used to refer to the left side of a stack, reading from left to right.  These elements might also be thought of as the "bottom" of the stack.  The word "back" is used to refer to the right side of a stack, reading from left to right.  These elements might also be thought of as the "top" of the stack.
