import math
from random import vonmisesvariate
def volume_cylinder(r = 'radius', h = 'height'):
    if r < 0 or h < 0:                      #test to make sure te input is positive integer
        print('Only positive integer is allowed for both values')
        return None
#     else:
#         print(f'radius = {r}, height = {h}')
#         volume = math.pi * r**2 * h         #calculating volume of cylinder in cm3
#         print(f'volume of the cylinder is {volume}')
#         return volume
        
volume_cylinder(-3, 4)
# print(volume_cylinder(5, 6))
# print(volume_cylinder(3, 7))
# print(volume_cylinder(7, 20))
