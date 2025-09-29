from turtle import *

def star(shape, width, size, color):
    shape.color(color)
    shape.width(width)
    shape.begin_fill()
    for i in range(5):
        shape.forward(size)
        shape.left(144)
    shape.end_fill()

def circle(shape, radius, color):
    shape.color(color)
    shape.begin_fill()
    shape.circle(radius)
    shape.end_fill()

t = Turtle()
shape = input('Enter your desire shape: ')

while True:
    if shape == 'finish':
        print('Drawing Ended')
        break
    elif shape == 'star':
        width = int(input('Enter Width: '))
        size = int(input('Enter Size: '))
        colour = input('Enter Colour: ')
        star(t, width, size, colour)
    elif shape == 'square':
        radius = int(input('Enter Radius: '))
        colour = input('Enter Colour: ')
        circle(t, radius, colour)
    else:
        print('Invalid shape entered !')

done()
