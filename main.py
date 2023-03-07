from breakout import Bar, Ball, Walls, Board
import turtle
from time import sleep


def play_game():
    screen = turtle.Screen()
    screen.title('Breakout Game')
    screen.setup(900, 787)
    screen.tracer(0)
    bar = Bar()
    ball = Ball()
    walls = Walls()
    board = Board()

    # Getting the keys
    screen.onkey(fun=bar.move_l, key='a')
    screen.onkey(fun=bar.move_l, key='Left')
    screen.onkey(fun=bar.move_r, key='d')
    screen.onkey(fun=bar.move_r, key='Right')
    screen.listen()

    game_is_on = True

    while game_is_on:
        sleep(0.03)
        screen.update()
        ball.move()
        if ball.ycor() <= bar.ycor() + 25 and 50 > abs(ball.xcor()-bar.xcor()):
            ball.collision_down()
        if ball.xcor() <= -440 or ball.xcor() >= 440:
            ball.collision_side()
        if ball.ycor() < -400 or ball.ycor() >= 382:
            game_is_on = False
        for wall in walls.walls:
            if wall.distance(ball) < 50:
                ball.collision_down()
                walls.lost_part(wall)
                board.up_score()

    board.end_game()

    screen.exitonclick()


if __name__ == '__main__':
    play_game()
