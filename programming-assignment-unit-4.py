
"""
**************************
CS1101 - Programming Assignment Unit 4
**************************

Do Exercise 6.4 from your textbook using recursion and the is_divisible function from Section 6.4.  Your program may assume that both arguments to is_power are positive integers. Note that every positive integer that has an exponent of 0 is a power of "1". This includes "0" and "1", itself.

A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.

You should submit a script file and a plain text output file (.txt) that contains the test output. Multiple file uploads are permitted. Don’t forget to include descriptive comments in your Python code.

**************************
1. Does the submission include the is_divisible function from Section 6.4 of the textbook?
2. Does the submission implement an is_power function that takes two arguments?
3. Does the is_power function call is_divisible?
4. Does the is_power function call itself recursively?
5. Does the is_power function include code for the base case of the two arguments being equal?
6. Does the is_power function include code for the base case of the second argument being "1"?
7. Does the submission include correct output for the five test cases?
**************************

**************************
Link to image of output:
https://www.dropbox.com/s/23zght81ydju89s/pa-u4-output.png?dl=0
**************************

"""


# This version isn't necessary
# def is_divisible(x, y):
#     if x % y == 0:
#         return True
#     else:
#         return False

def is_divisible(a, b):
    # No conditional necessary; this patter already returns True or False
    return a % b == 0


# Only positive integers
# Does the submission implement an is_power function that takes two arguments?
def is_power(a, b):
    # Does the is_power function call is_divisible
    if not is_divisible(a, b):
        return False
    # Does the is_power function include code for the base case of the two arguments being equal?
    if b == a:
        return True
    # Does the is_power function include code for the base case of the second argument being "1"?
    elif b == 1:
        return False
    # Does the is_power function call itself recursively?
    return is_power(int(a/b), b)


print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))


"""
Link to image of output:
https://www.dropbox.com/s/23zght81ydju89s/pa-u4-output.png?dl=0
"""