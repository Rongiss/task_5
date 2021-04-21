import turtle


def main():
    # Няжняя часть
    drawe_base(0, -80, 80)
    # Туловеще
    drawe_base(0, 80, 40)
    # Голова
    drawe_base(0, 160, 30)
    # Правый глаз
    drawe_base(15, 195, 5)
    # Левый глаз
    drawe_base(-15, 195, 5)
    # Нижняя часть
    shapka(-45, 210, 90, 10)
    # Верхняя часть
    shapka(-25, 220, 50, 40)

    left_hend(40, 120)
    rith_hend(-40, 120)
    mos = 20
    mouth(-10, 180, mos)



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

def left_hend(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.left(120)
    turtle.forward(45)
    turtle.left(30)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(15)
    turtle.left(210)
    turtle.forward(15)

def rith_hend(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(150)
    turtle.forward(25)
    turtle.setheading(130)
    turtle.forward(25)
    turtle.setheading(125)
    turtle.forward(15)
    turtle.setheading(180)
    turtle.forward(15)
    turtle.setheading(0)
    turtle.forward(15)
    turtle.setheading(195)
    turtle.forward(15)
    turtle.hideturtle()


def mouth(x, y, mos):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(mos)



main()
turtle.done()
