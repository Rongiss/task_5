import turtle

x = 0
y = 0
step = 8
long = 200
step_long = long / step
long_gip = (long ** 2 + long ** 2) ** 0.5

def main():
    sqare(x, y, step)
    line_and_gip(x, y, long, long_gip)
    second_sqare(x, y, step, long)
    third_sqare(x, y, step, long)

def line_and_gip(x, y, long, long_gip):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(45)
    turtle.pendown()
    turtle.forward(long_gip)

    turtle.penup()
    turtle.goto(x, long)
    turtle.setheading(315)
    turtle.pendown()
    turtle.forward(long_gip)

    turtle.penup()
    turtle.goto(x, long / 2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(long)

    turtle.penup()
    turtle.goto(long / 2, y)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(long)


def sqare(x, y, step):
    sq = 0
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.setheading(0)

    while sq < 4:
        turtle.forward(long)
        turtle.left(90)
        sq += 1

def second_sqare(x,y,step, long):
    sq = 0
    turtle.penup()
    turtle.goto(step_long, step_long)
    turtle.pendown()

    turtle.setheading(0)

    while sq < 4:
        turtle.forward(long - step_long * 2)
        turtle.left(90)
        sq += 1

def third_sqare(x,y,step, long):
    sq = 0
    turtle.fillcolor('black')
    turtle.penup()
    turtle.goto(step_long * 2, step_long * 2)
    turtle.pendown()

    turtle.setheading(0)
    turtle.begin_fill()
    while sq < 4:
        turtle.forward(long - step_long * 4)
        turtle.left(90)
        sq += 1
    turtle.end_fill()

main()

turtle.done()