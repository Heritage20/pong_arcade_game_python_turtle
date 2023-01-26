from turtle import Turtle


class Ball(Turtle):
    """defines the class of the ball inheriting from the turtle class"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """defines the ball movements and to x and y direction"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """defines what happens to the ball when it touches
        the edge of the wall decreasing the y movement
        """
        self.y_move *= -1

    def bounce_x(self):
        """defines what happens to the ball when it touches
        the paddle, decreasing the x movement and
        increasing the speed of the ball
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """ it resets the position of the ball to the starting
        point and the speed to the initial speed when the player misses
        the ball
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

