import turtle
# t = turtle.Turtle()
def square(t, length):
    # import turtle
    t = turtle.Turtle()
    # l = length
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

# square(6, 100)

def polygon(t, n, length):
    # import turtle
    t = turtle.Turtle()
    l = length
    angle = 360/n #exterior angle of an n-sided polygon
    for i in range(n):
        t.fd(l)
        t.lt(angle)
    turtle.mainloop()

# polygon('bob', n=7, length=70)

def arc(arci, radius):
    r = radius
    for i in range(arci):
        t = turtle.Turtle()
        t.fd(r)
        t.lt(1)
    # t.fd(r)
    turtle.mainloop()

# arc(180, 2)
import math

def circles(t, r):
    circumference =  2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

# circles(7, 80)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)

# circle(5, 20)

def arc(t, r, angle):
    t = turtle.Turtle()
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
    turtle.mainloop()

# arc(5, 80, 50)

def polyline(t, n, length, angle):
    t = turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)
    turtle.mainloop()

polygon(6, 15, 10)