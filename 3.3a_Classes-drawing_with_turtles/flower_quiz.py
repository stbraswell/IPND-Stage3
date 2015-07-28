import turtle

def draw_leaf(some_turtle):
    #for i in range (1,10):
    some_turtle.right(30)
    some_turtle.forward(100)
    some_turtle.circle(30,180)
    some_turtle.left(30)
    some_turtle.forward(100)
    some_turtle.right(140)


window = turtle.Screen()
window.bgcolor("white")
troy = turtle.Turtle()
troy.shape("circle")
troy.color("blue")
troy.speed(2)

troy1 = turtle.Turtle()
troy1.shape("circle")
troy1.color("blue")
troy1.circle(15)

draw_leaf(troy)

window.exitonclick()
