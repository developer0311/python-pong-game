from turtle import Screen
import time
from scoreboard import Scoreboard
from middleLine import MiddleLine
from paddle import Paddle
from ball import Ball


# all screen settings
screen = Screen()
screen.title("Pong")
screen.setup(width = 1000, height = 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# score management
score = Scoreboard()

# middle line  for seperating
middleLine = MiddleLine()


# setting left and right paddle
l_paddle = Paddle((-450, 0))
r_paddle = Paddle((450, 0))


# listening screen to movie left and right paddle
screen.onkeypress(r_paddle.move_up,"Up")
screen.onkeypress(r_paddle.move_down,"Down")
screen.onkeypress(l_paddle.move_up,"w")
screen.onkeypress(l_paddle.move_down,"s")


# creating a ball object
ball = Ball()


# tracing the game is on or off
game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # bouncing the ball respect to y axix
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # bouncing the ball respect to x axix if any paddle touvh it
    if ball.distance(r_paddle) < 50 and ball.xcor() > 420 or ball.distance(l_paddle) < 50 and ball.xcor() < -420:
        ball.bounce_x()

    # increasing left player's score if right player miss to hit the ball
    if ball.xcor() > 480:
        ball.reset_position()
        score.increaseLeftScore()
    # increasing right player's score if left player miss to hit the ball

    if ball.xcor() < -480:
        ball.reset_position()
        score.increaseRightScore()



screen.exitonclick()