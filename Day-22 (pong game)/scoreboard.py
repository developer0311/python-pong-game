from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 75, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.leftScore = 0
        self.leftColor = "white"
        self.rightScore = 0
        self.rightColor = "white"
        self.hideturtle()
        self.penup()
        self.update_soceboard()

    def update_soceboard(self):
        self.clear()
        self.goto(-80, 200)
        self.score_color()
        self.pencolor(self.leftColor)
        self.write(f"{self.leftScore}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(80, 200)
        self.pencolor(self.rightColor)
        self.write(f"{self.rightScore}", move=False, align=ALIGNMENT, font=FONT)

    def increaseLeftScore(self):
        self.leftScore += 1
        self.update_soceboard()

    def increaseRightScore(self):
        self.rightScore += 1
        self.update_soceboard()
    
    def score_color(self):
        if self.leftScore > self.rightScore:
            self.leftColor = "green2"
            self.rightColor = "red1"

        elif self.leftScore < self.rightScore:
            self.leftColor = "red1"
            self.rightColor = "green2"

        else:
            self.leftColor = "white"
            self.rightColor = "white"