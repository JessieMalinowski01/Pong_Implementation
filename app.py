import turtle
import time


# Set up the screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=600, height=400)

# Create the paddles
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-250, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(250, 0)

# Create the ball
ball = turtle.Turtle()
ball.speed(40)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Set up the score
left_score = 0
right_score = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 170)
score.write("Player 1: {}    Player 2: {}".format(
    left_score, right_score), align="center", font=("Courier", 16, "normal"))

# Move the paddles


def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)


def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)


def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)


# Bind the keys to the paddle movement functions
screen.listen()
screen.onkeypress(left_paddle_up, "w")
screen.onkeypress(left_paddle_down, "s")
screen.onkeypress(right_paddle_up, "Up")
screen.onkeypress(right_paddle_down, "Down")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collision with the walls
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Check for collision with the paddles
    if ball.xcor() < -240 and left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 240 and right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50:
        ball.dx *= -1

    # Check for scoring
    if ball.xcor() > 290:
        left_score += 1
        score.clear()
        score.write("Player 1: {}    Player 2: {}".format(
            left_score, right_score), align="center", font=("Courier", 16, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        time.sleep(1)

    if left_score == 5 or right_score == 5:
        score.clear()
        if left_score == 5:
            score.write("Player 1 wins!", align="center",
                        font=("Courier", 16, "normal"))
        else:
            score.write("Player 2 wins!", align="center",
                        font=("Courier", 16, "normal"))
        time.sleep(3)
        screen.bye()
