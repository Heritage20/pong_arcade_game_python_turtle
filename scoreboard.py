from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    """defines the class of the scoreboard inheriting from the turtle class"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """it sets the position of the scoreboard, alignment and fonts and
        initiates the clear method in turtle to update the scoreboard
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """defines the left paddle scoreboard and increases it by one based
        on the game outcome
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """defines the right paddle scoreboard and increases it by one based
        on the game outcome
        """
        self.r_score += 1
        self.update_scoreboard()
