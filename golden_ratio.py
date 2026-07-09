import turtle
import math

def draw_golden_spiral(t, n):
    """Draws a golden spiral using Fibonacci arcs."""
    # The first two dimensions for the squares
    a, b = 0, 1
    
    # We use these colors to clearly highlight the growing rectangles/arcs
    colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845']
    
    t.speed(3) # 1 is slowest, 10 is fast, 0 is instant
    t.pensize(2)
    
    for i in range(n):
        # Calculate the next dimension in the Fibonacci sequence
        a, b = b, a + b
        
        # Draw the Golden Rectangle
        t.pencolor(colors[i % len(colors)])
        for _ in range(2):
            t.forward(b * 5)
            t.right(90)
            t.forward(a * 5)
            t.right(90)
            
        # Draw the quarter circle (Arc) of the spiral
        # This approximates the Golden Spiral
        t.pencolor('black')
        t.circle(a * 5, 90)

# Setup the Turtle screen
screen = turtle.Screen()
screen.title("The Golden Spiral")
screen.bgcolor("white")

# Initialize the turtle
my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.goto(-200, -200) # Center the drawing
my_turtle.pendown()

# Run the function to draw 12 spiral segments
draw_golden_spiral(my_turtle, 12)

# Hide the turtle and wait for user to close window
my_turtle.hideturtle()
turtle.done()
