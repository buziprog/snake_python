from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Ardi's snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

###detect the collision with food






# starting_positions = [(0,0),(-20,0),(-40,0)]
#creating the snake body

# segments = []

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)


#moving the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    ###detecting collision with food

    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    ###detecting collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()< -280:

        scoreboard.reset()
        snake.reset()


    ####detecting collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment)<10:
            scoreboard.reset()


#####creating a scoreboard
# from turtle import Turtle
#
# class ScoreBoard(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color("white")
#         self.penup()
#         self.goto(0, 270)
#
#         self.write(f"Score {self.score}",align="center",font=("Arial",24,"normal"))
#         self.hideturtle()
#         self.update_scoreboard()
#
#     def update_scoreboard(self):
#
#         self.write(f"Score {self.score}",align="center",font=("Arial",24,"normal"))
#
#     def reset(self):
#         self.goto(0, 0)
#         self.write("GAME OVER",align="center",font=("Arial",24,"normal"))
#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()


#look at the code below once again
    # for segment_number in range(len(segments)-1, 0, -1):
    #     new_x = segments[segment_number - 1].xcor()
    #     new_y = segments[segment_number - 1].ycor()
    #     segments[segment_number].goto(new_x,new_y)
    # segments[0].forward(20)


######creating the classes
##### control the snake























screen.exitonclick()