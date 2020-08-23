#Sara Margaret Rizzo
#2020-08-22

#Problem 6: Use the polygon program from the last module and convert it to a function. 
#Call the function in a way to create a pattern similar to below.
import turtle

#function to draw hexagon
def drawHexagon(t, sz):
    for i in range(6):
        t.forward(sz)
        t.left(60)

#set up turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.pensize(3)
tess.color('hotpink')

size = 50

#the image is 10 overlapping hexagons, each tilted slightly
for i in range(10):
    drawHexagon(tess, size)
    #the hexagons sort of form a cirlce, so 360/10 is 36
    tess.right(36)

wn.exitonclick()