from turtle import Turtle

dx = 10
dy = 10


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        self.dx = dx
        self.dy = dy

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce(self):
        self.dx *= -1
        self.dy *= -1
