#Sara Margaret Rizzo
#2020-08-22

#Problem 5: Use the following chunk of code as a base to produce the image shown below.

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
#slow down for testing
#alex.speed(1) 

#draw 5 nested squares
#each square needs to be large than last
size = [20, 40, 60, 80, 100]

#for each item in list, draw the sqare
#then pick up pen, move to start next sqaure, repeat
for x in size:
    drawSquare(alex, x)
    alex.penup()
    alex.backward(10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()

wn.exitonclick()