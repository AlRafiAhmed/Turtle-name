import turtle

# Set up the turtle
t = turtle.Turtle()
t.pensize(5)
t.speed(3)

# Function to move turtle without drawing
def move_without_drawing(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Starting position
move_without_drawing(-200, 0)

# Draw 'A'
t.left(75)
t.forward(100)
t.right(150)
t.forward(100)
move_without_drawing(t.xcor() - 60, t.ycor() + 40)
t.right(105)
t.forward(40)

# Draw 'l'
move_without_drawing(t.xcor() + 20, 0)
t.left(90)
t.forward(80)

# Space
move_without_drawing(t.xcor() + 30, 0)

# Draw 'R'
t.left(90)
t.forward(80)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(135)
t.forward(60)

# Space
move_without_drawing(t.xcor() + 30, 0)

# Draw 'a'
t.left(45)
t.circle(20, 360)
t.forward(40)

# Draw 'f'
move_without_drawing(t.xcor() + 30, 0)
t.left(90)
t.forward(80)
t.right(90)
t.forward(30)
move_without_drawing(t.xcor() - 30, t.ycor() - 40)
t.forward(30)

# Draw 'i'
move_without_drawing(t.xcor() + 40, 0)
t.left(90)
t.forward(60)
move_without_drawing(t.xcor(), t.ycor() + 20)
t.circle(2)

# Space and move to next line
move_without_drawing(t.xcor() + 50, 0)

# Draw 'A'
t.left(75)
t.forward(100)
t.right(150)
t.forward(100)
move_without_drawing(t.xcor() - 60, t.ycor() + 40)
t.right(105)
t.forward(40)

# Draw 'h'
move_without_drawing(t.xcor() + 30, 0)
t.left(90)
t.forward(80)
t.backward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)

# Draw 'm'
move_without_drawing(t.xcor() + 30, 0)
t.left(90)
t.forward(60)
t.right(135)
t.forward(30)
t.left(90)
t.forward(30)
t.right(135)
t.forward(60)

# Draw 'e'
move_without_drawing(t.xcor() + 30, 0)
t.circle(20, 360)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)

# Draw 'd'
move_without_drawing(t.xcor() + 30, 0)
t.circle(30, 360)
t.left(90)
t.forward(80)

# Hide the turtle and keep window open
t.hideturtle()
turtle.done()
