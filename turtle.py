print("Attention: running only on jupyter-notebook\n\n\n\n\n\n\n\n")

import turtle
import random
from random import choice
def turtle_line():
    """this functions is drawing 4 random lines """
    wn = turtle.Screen()
    wn.bgcolor("lightgreen") # background color
    alex= turtle.Turtle()
    alex.pensize(5) # pensize
    alex.color("hotpink") # turtle color
    for i in range(4):
        r_l = choice(['left','right'])
        d = random.randrange(1, 361)
        if r_l == 'left':
            alex.left(d)
        else:
            alex.right(d)
        alex.forward(random.randrange(100, 200))
    turtle.exitonclick()
turtle_line()