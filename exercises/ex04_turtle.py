"""This image will be a picture of two moons in the sky over an alient planet's ocean at night."""

__author__ = "730316240"


from turtle import Turtle, colormode, done, tracer, update
from random import randint
colormode(255)


def night(turtle: Turtle, x: float, y: float, width: float) -> None:  # This functon will call the night function 
    """Draw the night background."""
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    color_i = 120
    turtle.color(122, 122, color_i)
    i: int = 0
    
    turtle.begin_fill()
    while(i < 4):
        turtle.forward(300)
        turtle.left(90)
        i = i + 1
        color_i += 5
    turtle.end_fill()
    
    return None


def moon(turtle: Turtle, x: float, y: float, width: float) -> None:  # This definition will call the function that will call the moon function 
    """Draws the moon.""" 
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(0, 3, 40)
    turtle.begin_fill()
    turtle.circle(width)
    turtle.position()
    turtle.end_fill()
   
    return None


def sea(turtle: Turtle, x: float, y: float, width: float) -> None:  # This definition will call the funciton that will create the sea in my picture 
    """Draws the sea at the bottom of the frame."""
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(0, 70, 223)
    t: int = 0
   
    turtle.begin_fill()
    while(t < 4):
        turtle.forward(x)
        turtle.left(90)
        t = t + 1
    turtle.end_fill()

    return None


def stars(turtle: Turtle, x: float, y: float, width: float) -> None:  # This function will create the stars in my sky 
    """Draws the stars in the sky."""
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(125, 76, 78)
    r: int = 0 
    n = 100

    while (r < n): 
        i = randint(100, 200)  # This is the loop that will create my stars. 
        turtle.penup()
        turtle.goto(i, i)
        turtle.pendown()
        turtle.dot(2, "yellow")
    r += 1

    return None


def frame(turtle: Turtle, x: float, y: float, width: float) -> None:  # This deinition will create the instructions to call forward my frame fucntion 
    """Creates the fram that will surround the picture."""
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(0, 0, 0)
    z: int = 0
    
    turtle.begin_fill()
    while z > 4: 
        turtle.forward(x)
        turtle.left(90)
        z = z + 1
    turtle.end_fill()

    return None


def main() -> None:  # This is the main function that will call all the previously defined variables and functions in order to create the image
    """This main function will call the moon, sea, stars, night and frame functions that I made in order to create my picture.""" 
    turtle: Turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(0)
    FRAME_X = -250
    FRAME_Y = 50
    FRAME_W = 600
    STAR_X = 2
    OCEAN_Y = 50
    MOON_X = 40
    MOON_Y = 85

    night(turtle, FRAME_X, FRAME_Y, FRAME_W)
    # stars(turtle, STAR_X, STAR_X, STAR_X)
    moon(turtle, MOON_X, MOON_X, MOON_X)
    moon(turtle, MOON_X, MOON_Y, MOON_X)
    sea(turtle, FRAME_X, OCEAN_Y, OCEAN_Y)
    frame(turtle, FRAME_X, FRAME_Y, FRAME_W)

    done()

    return None


if __name__ == "__main__":
    main()