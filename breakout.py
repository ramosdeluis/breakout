import random
import turtle
from turtle import Turtle


class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.turtle_basics()

    def turtle_basics(self):
        self.shape('square')
        self.turtlesize(1, 5, 2)
        self.penup()
        self.goto(0, -350)

    def move_l(self):
        if self.xcor() - 30 >= -420:
            self.goto(self.pos()[0] - 30, self.pos()[1])

    def move_r(self):
        if self.xcor() + 30 <= 410:
            self.goto(self.pos()[0] + 30, self.pos()[1])


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.turtle_basics()
        self.setheading(random.randrange(-135, -45))

    def turtle_basics(self):
        self.shape('square')
        self.penup()

    def move(self):
        self.forward(10)

    def collision_down(self):
        self.setheading(360*(1-(self.heading()/360)))

    def collision_side(self):
        self.setheading((180-self.heading()))


def wall_basics(a_turtle, num):
    from random import choice
    a_turtle.shape('square')
    a_turtle.turtlesize(2, 4, 2)
    a_turtle.penup()
    a_turtle.color(choice(['red', 'blue', 'green', 'LightSteelBlue', 'DarkCyan', 'Gold', 'DarkCyan', 'GreenYellow',
                           'PaleGreen', 'DarkRed', 'Purple', 'Plum', 'PaleVioletRed', 'Coral']))
    if (num // 11) % 2 != 0:
        a_turtle.goto((-420 + (85 * (num - (11 * (num // 11))))), (375 - 45 * (num // 11)))
    else:
        a_turtle.goto((-460 + (85 * (num - (11 * (num // 11))))), (375 - 45 * (num // 11)))


class Walls(Turtle):

    def __init__(self):
        super().__init__()
        self.walls = []
        self.hideturtle()

        for c in range(66):
            self.create_wall(c)

    def create_wall(self, num):
        a_turtle = turtle.Turtle()
        wall_basics(a_turtle, num)
        self.walls.append(a_turtle)

    def lost_part(self, wall):
        a, b, c = wall.shapesize()
        if a == 2:
            wall.turtlesize(1, b, c)
        elif a == 1:
            wall.turtlesize(0.5, b, c)
        else:
            wall.hideturtle()
            del self.walls[self.walls.index(wall)]


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(350, -300)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    # Define a function to update the scoreboard
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def up_score(self):
        self.score += 1
        self.update_score()

    def end_game(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"  END GAME!\nYour Score: {self.score}", align="center", font=("Courier", 24, "normal"))


if __name__ == '__main__':
    pass
