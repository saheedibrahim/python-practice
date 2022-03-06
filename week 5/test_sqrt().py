# Write your code here :-)
def my_sqrt(a): # Defining a function that takes in a parameter value.
    x = a
    while True:
        y = (x + a/x) / 2.0
        if y == x: # Comparison operator that checks whether x is equal to y.
            break
        x = y
    return x

#Testing Function
def test_sqrt():
    import math
    a = 1
    while a <= 25:
         b = my_sqrt(a)  # Takes the square root from the first function
         c = math.sqrt(a) # Takes Square root from math module
         dif = abs(c - b) # Takes the difference of the absolute value between b and c
         print('a =', a,'| my_sqrt(a) =', b ,'| math.sqrt(a) =', c ,'| diff =', dif)
         a += 1 #  Incremental operator
    return 0

test_sqrt() # Function invokation
