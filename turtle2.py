print("\n\n\nNote: this code running only in jupyter notebook\n\n\n\n\n")
import turtle
def turtle2():
	wn = turtle.Screen()
	t = turtle.Turtle()
	t.color('blue')
	t.shape('turtle')
	dist = 5
	t.up()
	for _ in range(100):
	    t.stamp()
	    t.forward(dist)
	    t.right(24)
	    dist += 2
	wn.exitonclick()
turtle2()