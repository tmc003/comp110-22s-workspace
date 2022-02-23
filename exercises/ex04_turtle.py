"""This image will be a picture of two moons in the sky over an alient planet's ocean at night.

I used different turtle functions on by using the turtle.circle function as welll as the accomponied position() code on line 49 and 50.
In my star function I chose to hide the turtle that creates the stars on line 81 and used the turtle.dot code to make my stars on line 90."""

__author__ = "730316240"


from turtle import Turtle, colormode, tracer, update, done
from random import randint
colormode(255)
MAX_SPEED = 0


def night(turtle: Turtle, x: float, y: float, width: float) -> None:  # This functon will call the night function 
    """Draw the night background."""
    turtle.speed(MAX_SPEED)
    turtle.penup()
    turtle.goto(-320, -320)
    turtle.pendown()
    color_r = 45
    color_g = 60
    color_b = 87
    turtle.color(color_r, color_g, color_b)
    i: int = 0
    
    turtle.begin_fill()
    while(i < 4):
        turtle.forward(700)
        turtle.left(90)
        i = i + 1
        color_g += 20
        color_b += 20
        color_r += 20
    turtle.end_fill()
    
    return None


def moon(turtle: Turtle, x: float, y: float, width: float) -> None:  # This definition will call the function that will call the moon function 
    """Draws the moon.""" 
    turtle.speed(MAX_SPEED)
    turtle.penup()
    axis_x: float = randint(-200, 200)
    axis_y: float = randint(-200, 200)
    turtle.goto(axis_x, axis_y)
    turtle.pendown()
    turtle.color(221, 245, 200)
    turtle.begin_fill()
    turtle.circle(width)
    turtle.position()
    turtle.end_fill()
   
    return None


def sea(turtle: Turtle, x: float, y: float, width: float) -> None:  # This definition will call the funciton that will create the sea in my picture 
    """Draws the sea at the bottom of the frame."""
    turtle.speed(MAX_SPEED)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    t: int = 0
    turtle.begin_fill()
    while(t < 3):
        turtle.tilt(45)
        turtle.shape("triangle")
        turtle.position()
        turtle.left(120)
        turtle.fillcolor(54, 100, 56)
        t = t + 1
    turtle.end_fill()

    return None


def stars(turtle: Turtle, x: float, y: float, width: float) -> None:  # This function will create the stars in my sky 
    """Draws the stars in the sky."""
    turtle.speed(MAX_SPEED)
    turtle.hideturtle()
    r: int = 0 
    n = 400
    while (r < n): 
        axis_y = randint(-300, 300)  # This is the loop that will create my stars. 
        axis_x = randint(-300, 300)
        turtle.penup()
        turtle.goto((axis_x), axis_y) 
        turtle.pendown()
        turtle.dot(3, "yellow")
        r += 1

    return None


def frame(turtle: Turtle, x: float, y: float, width: float) -> None:  # This deinition will create the instructions to call forward my frame fucntion 
    """Creates the fram that will surround the picture."""
    turtle.pensize(8)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.pencolor(24, 18, 22)
    z: int = 0
    
    while z > 4:
        turtle.forward(100)
        turtle.right(90)
        z = z + 1

    return None


def main() -> None:  # This is the main function that will call all the previously defined variables and functions in order to create the image
    """This main function will call the moon, sea, stars, night and frame functions that I made in order to create my picture.""" 
    turtle: Turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(MAX_SPEED)
    FRAME_X = 200
    FRAME_Y = 200
    FRAME_W = 200
    STAR_X = 2
    OCEAN_Y = 100
    MOON_X = 60
    MOON_Y = 85

    tracer(0, 0)

    night(turtle, FRAME_X, FRAME_Y, FRAME_W)
    stars(turtle, STAR_X, STAR_X, STAR_X)
    moon(turtle, MOON_X, MOON_X, MOON_X)
    moon(turtle, MOON_X, MOON_Y, MOON_X)
    sea(turtle, FRAME_X, OCEAN_Y, OCEAN_Y)
    frame(turtle, FRAME_X, FRAME_Y, FRAME_W)

    update()

    done()

    return None


if __name__ == "__main__":
    main()