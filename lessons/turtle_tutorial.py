from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()
colormode(255)

leo.color(122, 122, 122)
leo.pencolor("pink")
bob.color(255, 255, 255)
bob.pencolor("orange")

leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
leo.hideturtle()
leo.speed(0)
leo.begin_fill()
while(i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob.penup()
bob.goto(45, 60)
bob.pendown()

w: int = 0
while(w < 3):
    bob.forward(300)
    bob.left(120)
    w = w + 1

side_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1


# leo.forward(500)
# leo.left(90)
# leo.forward(500)
# leo.left(90)
# leo.forward(500)
# leo.left(90)
# leo.forward(500)
# leo.left(90)

done()