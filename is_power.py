def is_divisible(a,b):
    return a % b == 0 # checks to see if a is divisible evenly by b

def is_power(a,b):
    if b == a: # if b and a are equal it equals True. First base case.
        return True
    elif b == 1: # if b is 1 it returns False. Second base case
        return False
    elif is_divisible(a,b) and (a/b) % b**2 == 0: #runs is_divisible function and checks if powers of b are divisble
        return True
    else:
        return False # All other cases go to False

is_power(27, 3)

    
