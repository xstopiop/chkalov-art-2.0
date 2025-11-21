import time
import turtle
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor('Aquamarine')
turtle.tracer(0,0)
t = turtle.Turtle()
t.speed('fastest')
t.color('Violet')
t.pendown()
t.hideturtle()

t2 = turtle.Turtle()
t2.speed('fastest')

t.goto(0, -250)

def teeth(tcount = 50):
    for i in range(tcount):
        t.forward(10)
        #t.left(3)
        for j in range(3):
            t.forward(100)
            t.left(100)


def frame(openwidth):
    teeth()

    t.left(90)
    t.forward(openwidth)
    t.left(90)
    teeth()
    t.left(90)
    t.forward(openwidth)
    t.left(90)

t2.color('violet')
t2.forward(50)

for i in range(50):
    frame(100)
    turtle.update()
    time.sleep(1.0)
    t.clear()
    frame(100)
    turtle.update()
    time.sleep(1.0)
    t.clear()
    frame(100)
    turtle.update()
    time.sleep(0.1)
    t.clear()
    frame(20)
    turtle.update()
    time.sleep(0.1)



t.penup()


turtle.done()
