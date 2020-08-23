#Sara Margaret Rizzo
#2020-08-22

#Problem 1: Write a function areaOfCircle(r) which returns the area of a circle of radius r. 
#Make sure you use the math module in your solution.

#use math module, need for pi
import math

#function that calculates area of circle, area = pi*r^2
def area(r):
    a = math.pi * r**2
    return a

#ask user for radius, change type to integer
r = int(input("What is the radius of the circle? "))

#take input, calculate area
result = area(r)
print("The area of the circle is", result)



