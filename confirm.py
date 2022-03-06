def is_divisible(x, y):

    if x % y == 0:

        return True

    else:

        return False

#The is_power function is checking the divisibility between two numbers

def is_power(a,b):

    #The numbers a and b must be positive integers

    if a>=0 and b>=0:

        return is_divisible(a,b)

        #The function is recursive

        return is_power(a/b,b)

    else: print('please try again using only positive Integers')

print("is_power(10, 2) returns: ", is_power(10, 2))

print("is_power(27, 3) returns: ", is_power(27, 3))

print("is_power(1, 1) returns: ", is_power(1, 1))

print("is_power(10, 1) returns: ", is_power(10, 1))

print("is_power(3, 3) returns: ", is_power(3, 3))