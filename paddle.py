from turtle import Turtle


class Paddle(Turtle):
    """defines the class of the paddle inheriting from the turtle class"""

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """defines the direction of the paddle when the player
        presses the key input specified on the keyboard
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """defines the direction of the paddle when the player
            presses the key input specified on the keyboard
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)