import turtle
import random

def draw_fractal_tree(branch_len, pen_size, t):
    """
    Recursively renders binary branching vectors with randomized physics deviations 
    mimicking authentic growth algorithms.
    """
    if branch_len > 10:
        # Dynamically scale pen thickness as branches narrow down
        t.pensize(pen_size)
        
        # Color shifting based on length (Brown for trunk, Green for leaves)
        if branch_len < 25:
            t.pencolor("#2E8B57") # SeaGreen leaf tone
        else:
            t.pencolor("#8B4513") # SaddleBrown wood tone
            
        # Draw forward branch vector
        t.forward(branch_len)
        
        # Calculate random variances for authentic organic asymmetries
        angle_right = random.randint(15, 35)
        angle_left = random.randint(15, 35)
        length_reduction = random.uniform(0.7, 0.85)
        
        # Sub-branch generation routing (Right Node)
        t.right(angle_right)
        draw_fractal_tree(branch_len * length_reduction, pen_size * 0.75, t)
        
        # Sub-branch generation routing (Left Node)
        t.left(angle_right + angle_left)
        draw_fractal_tree(branch_len * length_reduction, pen_size * 0.75, t)
        
        # Reset relative positional parameters back to root node coordinates
        t.right(angle_left)
        t.pencolor("#8B4513")
        t.backward(branch_len)

def main():
    # Setup canvas viewport
    screen = turtle.Screen()
    screen.bgcolor("#F5F5DC") # Clean Ivory backdrop
    screen.title("Algorithmic Organic Tree Generator")
    
    # Instantiate Turtle parameters
    yggdrasil = turtle.Turtle()
    yggdrasil.speed(0)
    screen.tracer(5, 0) # Accelerates structural trace render speeds
    
    # Reposition Turtle base to ground level facing upwards
    yggdrasil.left(90)
    yggdrasil.up()
    yggdrasil.backward(180)
    yggdrasil.down()
    
    # Initiate recursive generation (Trunk Length, Initial Thickness, Turtle Instance)
    draw_fractal_tree(100, 12, yggdrasil)
    
    yggdrasil.hideturtle()
    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    main()
