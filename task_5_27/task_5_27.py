import turtle
import random
windows_x = 600
windows_y = 600
color_bg = 'black'
color_star = 'white'

turtle.setup(windows_x, windows_y)

turtle.bgcolor(color_bg)

def main():
    star()
    city()

def star():
    turtle.speed(0)
    turtle.penup()
    for i in range(0, 20):
        x = random.randint(-windows_x / 2, windows_y / 2)
        y = random.randint(-windows_x / 2, windows_y / 2)
        turtle.goto(x, y)
        step = 0
        turtle.setheading(0)
        turtle.fillcolor(color_star)
        turtle.begin_fill()
        while step < 4:


            turtle.forward(5)
            turtle.left(90)
            step += 1
        turtle.end_fill()

def city():
    turtle.speed(2)
    start_x = - windows_x / 2
    start_y = - windows_y / 2

    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.setheading(0)
    turtle.pencolor('white')
    turtle.pendown()
    turtle.goto(- start_x, start_y)
    turtle.setheading(90)
    turtle.goto(- start_x, start_y * 0)
    turtle.setheading(180)
    turtle.goto(start_x, start_y * 0)
    turtle.setheading(270)
    turtle.goto(start_x, start_y)
    turtle.end_fill()

main()
#turtle.goto(0, 0)
turtle.done()