import turtle
import time
import random

# Set up the screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []
score = 0

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "bold"))

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# Main Game Loop
while True:
    win.update()

    # Border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "bold"))

    # Eating food
    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "bold"))

    # Move body segments
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "Stop"
            for s in segments:
                s.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Courier", 24, "bold"))

    time.sleep(0.1)
