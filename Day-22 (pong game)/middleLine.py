from turtle import Turtle

DOT_SIZE = 5
DOWN_POSITION = 0

class MiddleLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("yellow")
        self.pensize(2)
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.pendown()
        self.line()

    def line(self):
        while self.ycor() < 280:
            self.forward(10)
            self.penup()
            self.forward(15)
            self.pendown()