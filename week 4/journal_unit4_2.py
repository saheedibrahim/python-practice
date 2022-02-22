import math
def volume_cylinder(r = 'radius', h = 'height'):
    if r < 0 or h < 0:                      #test to make sure te input is positive integer
        return None
    else:
        volume = math.pi * r**2 * h         #calculating volume of cylinder in cm3
        return volume
        
print(volume_cylinder(5, 6))
print(volume_cylinder(3, 7))
print(volume_cylinder(7, 20))
