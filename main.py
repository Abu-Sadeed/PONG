import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

paddle_1 = Paddle((-380, 0))
paddle_2 = Paddle((380, 0))

screen.listen()
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")
screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")

ball = Ball((0, 0))
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

screen.exitonclick()
