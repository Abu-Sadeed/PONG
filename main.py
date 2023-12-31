import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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

scoreboard = Scoreboard()
game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.dy *= -1

    if ball.distance(paddle_2) < 50 and ball.xcor() > 345 or ball.distance(paddle_1) < 50 and ball.xcor() < -345:
        ball.dx *= -1

    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.move_speed *= 0.9
        scoreboard.l_score_update()

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.move_speed *= 0.9
        scoreboard.r_score_update()

    if scoreboard.r_score >= 10 or scoreboard.l_score >= 10:
        game_on = False
        scoreboard.game_over(
            "Player L" if scoreboard.l_score >= 10 else "Player R")

screen.exitonclick()
