def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def is_power(a, b):
    if a < 0 or b < 0:
        return ('The two integers should be positive')
    if a == 1 and b == 1:
        return True
    elif a != 1 and b == 1:
        return False
    elif  is_divisible(a, b) == False:
            return False
    else:
        n = a / b
        if n == 1:
            return True
        elif n % b != 0:
            return False
        else:
            if n % b == 0:
                is_power(n, b)
                return True

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))