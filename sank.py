import turtle
import time
import random

# Screen setup
s = turtle.Screen()
s.title('Snake Game')
s.bgcolor('white')
s.setup(width=600, height=600)
s.tracer(0)

# Variables
delay = 0.1
score = 0
high_score = 0

# Snake head
head = turtle.Turtle()
head.shape('square')
head.color('blue')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake food
food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.goto(100, 0)

# Snake body
segments = []

# Scoreboard
sb = turtle.Turtle()
sb.speed(0)
sb.color('black')
sb.penup()
sb.hideturtle()
sb.goto(-250, 250)
sb.write('Score: 0  High Score: 0', align='left', font=('Arial', 14, 'normal'))

# Movement functions
def move():
    if head.direction == 'up':
        head.sety(head.ycor() + 20)
    if head.direction == 'down':
        head.sety(head.ycor() - 20)
    if head.direction == 'left':
        head.setx(head.xcor() - 20)
    if head.direction == 'right':
        head.setx(head.xcor() + 20)

def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

# Keyboard bindings
s.listen()
s.onkey(go_up, 'Up')
s.onkey(go_down, 'Down')
s.onkey(go_left, 'Left')
s.onkey(go_right, 'Right')

# Main game loop
while True:
    s.update()

    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'
        for segment in segments:
            segment.hideturtle()
        segments.clear()
        score = 0
        delay = 0.1
        sb.clear()
        sb.write(f'Score: {score}  High Score: {high_score}', align='left', font=('Arial', 14, 'normal'))

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        segment = turtle.Turtle()
        segment.shape('square')
        segment.color('green')
        segment.penup()
        segments.append(segment)

        score += 10
        if score > high_score:
            high_score = score

        sb.clear()
        sb.write(f'Score: {score}  High Score: {high_score}', align='left', font=('Arial', 14, 'normal'))

        delay -= 0.001

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            for segment in segments:
                segment.hideturtle()
            segments.clear()
            score = 0
            delay = 0.1
            sb.clear()
            sb.write(f'Score: {score}  High Score: {high_score}', align='left', font=('Arial', 14, 'normal'))

    time.sleep(delay)

s.mainloop()
