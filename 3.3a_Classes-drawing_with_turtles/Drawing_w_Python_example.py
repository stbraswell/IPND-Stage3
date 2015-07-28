import turtle     #turtle is what actually moves around and draws, why turtle?

def draw_square():
    window = turtle.Screen()   #window screen
    window.bgcolor("red")   #gives window screen a red background
    
    brad = turtle.Turtle()  #he called this grabbing a turtle
    brad.shape("turtle")    #changes the shape of the line leader
    brad.color("blue")      #changes the color of the line and line leader
    brad.speed(2)           #changes the speed of brad

    i = 1
    while i <= 4:
        brad.forward(100)       # this moves the turtle(aka brad?) forward a distance
        brad.right(90)          #turns brad right 90 degrees
        i += 1

    # create angie the turtle and make her a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)

    # create jay the turtle
    jay = turtle.Turtle()      
    jay.shape("triangle")
    jay.color("black")


    i = 1
    # make jay draw a triangle
    while i <= 3:
        jay.forward(100)
        jay.left(120)
        i += 1
    
    window.exitonclick()    #closes window any time you click on it
draw_square()
