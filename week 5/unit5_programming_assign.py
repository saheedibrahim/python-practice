import math


def my_sqrt(a):
    x = 1
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
    return y


def test_sqrt():
    for a in range(1, 25):
        m = my_sqrt(a)
        s = math.sqrt(a)
        print(
            f'a = {a} | my_sqrt(a) = {m} | math.sqrt(a) = {s} | diff {abs(m - s)}')


test_sqrt()
