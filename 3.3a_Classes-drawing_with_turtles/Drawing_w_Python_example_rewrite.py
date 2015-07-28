import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()   #window screen
    window.bgcolor("red")   #gives window screen a red background
    # create brad the turtle
    brad = turtle.Turtle()  #he called this grabbing a turtle
    brad.shape("turtle")    #changes the shape of the line leader
    brad.color("blue")      #changes the color of the line and line leader
    brad.speed(2)           #changes the speed of brad

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    # create angie the turtle and make her a circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("yellow")
    #angie.circle(100)

    window.exitonclick()    #closes window any time you click on it

draw_art()
