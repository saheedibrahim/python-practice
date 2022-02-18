import turtle
# t = turtle.Turtle()
def draw(t, length, n):
    t = turtle.Turtle()
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)
turtle.mainloop()

draw(5, 4, 5)
