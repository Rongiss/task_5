import turtle


def main():

    drawe_base(0, -80, 80)
    drawe_base(0, 80, 40)
    drawe_base(0, 160, 30)
    drawe_base(15, 195, 5)
    drawe_base(-15, 195, 5)
    shapka(-45, 210, 90, 10)
    shapka(-25, 220, 50, 40)


def drawe_base(x, y, cirk):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(cirk)
    turtle.penup()

def shapka(x, y, long, short):
    turtle.setheading(0)
    turtle.speed(5)
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(long)
    turtle.left(90)
    turtle.forward(short)
    turtle.left(90)
    turtle.forward(long)
    turtle.left(90)
    turtle.forward(short)

    turtle.end_fill()



main()
turtle.done()
