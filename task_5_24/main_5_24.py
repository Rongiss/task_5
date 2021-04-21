import turtle
import math

kat_long = 240
gip = (kat_long ** 2 + kat_long ** 2) ** 0.5
color1 = 'red'
color2 = 'green'
def main():
    big_tiangle(kat_long, gip)
    left_triangle(0, kat_long, color1)
    rith_triangle(0, kat_long, color2)

def big_tiangle(kat_long, gip):
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.forward(kat_long)
    turtle.setheading(135)
    turtle.forward(gip)
    turtle.setheading(225)
    turtle.forward(gip)
    turtle.setheading(0)
    turtle.forward(kat_long)
    turtle.end_fill()

def left_triangle(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(kat_long)
    turtle.setheading(180)
    turtle.forward(kat_long)
    turtle.setheading(315)
    turtle.forward(gip)
    turtle.end_fill()

def rith_triangle(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(kat_long)
    turtle.setheading(0)
    turtle.forward(kat_long)
    turtle.setheading(-135)
    turtle.forward(gip)
    turtle.end_fill()
main()
turtle.done()



