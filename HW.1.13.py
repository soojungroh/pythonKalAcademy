import turtle

turtle.pensize(5)

def drawLine(x,y):
    turtle.pendown()
    turtle.goto(x,y)
    turtle.penup()
    turtle.goto(0,0)

    

drawLine(0,50)
drawLine(50,0)
drawLine(-50,0)
drawLine(0,-50)

turtle.done()
