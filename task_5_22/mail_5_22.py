import turtle

def main():
    x = 0
    y = 0
    color = 'Red'
    tiangle(x, y, color)

def tiangle(x, y, color):
    print(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(150)
        turtle.left(120)
    turtle.end_fill()

main()
turtle.done()