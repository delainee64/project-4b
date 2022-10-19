# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/18/2022
# Description: Write a function named fib that takes a positive
# integer parameter and returns the number at that position of the Fibonacci sequence.

def fib(pos_int):
    """ Function returns a positive integer in the correct position in
    the Fibonacci sequence"""
    var_1 = 0
    var_2 = 1
    if pos_int <= 2:  # accounts for the first and second fib sequence being 1
        return 1
    else:
        for terms in range(2, pos_int + 1):  # set terms
            var_3 = var_1 + var_2
            var_1 = var_2
            var_2 = var_3
        return var_2

# print(fib(1))
# print(fib(3))
# print(fib(10))
# print(fib(17))
