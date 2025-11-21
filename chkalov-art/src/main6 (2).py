import turtle

screen = turtle.Screen()
screen.title("Черепашка-художник")
screen.bgcolor("white")
screen.setup(width=1280, height=800)
screen.tracer(0)

t = turtle.Turtle()
t.shape("turtle")
t.color("purple")
t.pensize(3)
t.pendown()
t.speed(0)

def go_forward():
    t.forward(15)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

def toggle_pen():
    if t.isdown():
        t.penup()
        t.color("gray")
    else:
        t.pendown()
        t.color("purple")

def clear_all():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    t.color("purple")

def quit_gracefully():
    screen.clear()
    screen.bgcolor("black")
    text = turtle.Turtle()
    text.hideturtle()
    text.color("gold")
    text.penup()
    text.goto(0, 0)
    text.write("\nСпасибо за творчество!", 
               align="center", font=("impact", 20, "bold"))
    screen.ontimer(screen.bye, 2000)

screen.listen()
screen.onkey(go_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(toggle_pen, "space")
screen.onkey(clear_all, "c")
screen.onkey(quit_gracefully, "Escape")

def update():
    screen.update()
    screen.ontimer(update, 30)

update()

screen.exitonclick()