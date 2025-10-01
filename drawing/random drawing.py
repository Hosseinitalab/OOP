from turtle import Turtle, done
from random import randint

class drawing(Turtle):
    def __init__(self):
        super().__init__()
        self.shape = input('Enter your desire shape: ')
        self.repetition = int(input('Enter the Repetition: '))
        if self.shape == 'star':
            self.w = int(input('Enter Width: '))
            self.s = int(input('Enter Size: '))
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
            
            self.color(r, g, b)
            self.width(self.w)
            self.up()
            self.goto(x, y)
            self.down()
            self.begin_fill()
            for i in range(5):
                self.forward(self.s)
                self.left(144)
            self.end_fill()

pencil = drawing()
