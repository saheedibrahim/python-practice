def my_sqrt(a): # finding the square root of a
    x = 6
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return y

import math
def test_sqrt():
    a = 1
    while a <= 25:
        my_sqrt(a)
        diff = abs(my_sqrt(a) - math.sqrt(a))
        print(f'a = {a} | my_sqrt(a) = {my_sqrt(a)} | math.sqrt(a) = {math.sqrt(a)} | diff = {diff}')
        a += 1

test_sqrt()
