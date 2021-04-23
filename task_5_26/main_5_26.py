# Шахматная доска
import turtle

y = 0
long = 40
#color = 'black'
def main():

    draw_sqare()

def draw_sqare():
    color = 'black'
    for j in range(0, long * 5, long):
        y = j

        for i in range(0, long * 5, long):
            turtle.penup()
            turtle.goto(i, y)
            turtle.pendown()
            step = 0
            turtle.setheading(0)

            turtle.fillcolor(color)
            turtle.begin_fill()

            while step < 4:


                turtle.forward(long)
                turtle.left(90)
                step += 1

            turtle.end_fill()
            if color == 'black':
                color = 'white'
            else:
                color = 'black'


main()
turtle.done()