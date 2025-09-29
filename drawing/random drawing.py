from turtle import *
from random import randint

class drawing():
    def __init__(self):
        self.object = Turtle()
        self.shape = input('Enter your desire shape: ')
        self.repetition = int(input('Enter the Repetition: '))
        if self.shape == 'star':
            self.width = int(input('Enter Width: '))
            self.size = int(input('Enter Size: '))
            self.star()
        else:
            print('Invalid Shape.')
        done()

    def star(self):
        for i in range(self.repetition):
            r = randint(0, 255)/255
            g = randint(0, 255)/255
            b = randint(0, 255)/255
            x = randint(-200, 200)
            y = randint(-200, 200)
            
            self.object.color(r, g, b)
            self.object.width(self.width)
            self.object.up()
            self.object.goto(x, y)
            self.object.down()
            self.object.begin_fill()
            for i in range(5):
                self.object.forward(self.size)
                self.object.left(144)
            self.object.end_fill()

pencil = drawing()
