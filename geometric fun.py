import turtle
import colorsys

# Setup the window and turtle
turtle.title("Trippy Rainbow Spiral")
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
turtle.tracer(2, 0) # Speeds up drawing significantly

# Draw the spiral
h = 0
for i in range(400):
    color = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    t.pencolor(color)
    h += 0.005
    t.forward(i)
    t.right(119) # Changing this angle changes the entire pattern!

turtle.done()
