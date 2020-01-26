# generate_uniform_random_numbers.py
# 24 July 2018

from random import randint

def generate_uniform_random_numbers(a, b):
    """Generates a uniform random number in the inclusive range [a,b].

        Args:
            a: integer
            b: integer strictly greater than argument a

        Returns: integer in the inclusive range [a,b]

        Raises:
            TypeError: Expecting two integers
            ValueError: Second argument must be greater than the first
    """
    num_generated = b - a + 1
    while True:
        random_num, i = 0, 0
        while (1 << i) < num_generated:
            random_num = (random_num << 1) | randint(0,1)
            i += 1
        if random_num < num_generated:
            break
    return random_num + a
