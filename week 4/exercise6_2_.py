import math
from unittest import result

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

# print(distance(1, 2, 4, 6))

# radius = distance()
def area(radius = distance(1, 2, 4, 6)):
    area_circle = math.pi * radius**2
    return area_circle
    
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

circle_area(1, 2, 4, 60)


# print(area(1,2,4,6))
print(circle_area(1, 2, 4, 6))