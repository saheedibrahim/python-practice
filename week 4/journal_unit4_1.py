import math

def hypotenuse(opp, adj):
    print(f'The opposite value is {opp} and the adjacent value is {adj}')
    x = opp**2
    y = adj**2
    print(f'The square of the opposite value is {x} and the square of the adjacent value is {y}')
    hyp = math.sqrt(x + y) #computing, uing pythagoras theorem hypothenus^2 = oppoite^2 + adjacent^2
    print(f'The hypotenuse is {hyp}')
    # return hyp

hypotenuse(3, 4)
# print(hypotenuse(3, 4), '\n')
# print(hypotenuse(6, 8), '\n')
# print(hypotenuse(9, 14), '\n')
