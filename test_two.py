from turtle import *
from random import randint

s_width = 200
s_height = 180


class Sprite(Turtle):
    def __init__(self, x, y, shape, color):
        Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.left(180)
        self.step = 10
        self.points = 0
class Enemy(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = 20
        self.speed(10)


player = Sprite(170, 160, 'turtle', 'green')
enemy1 = Enemy(s_width, -90, 'triangle', 'red')
enemy1.move(s_width, -90, -s_width, -90)
enemy2 = Enemy(-s_width, 90, 'triangle', 'red')
enemy2.move(-s_width, 90, s_width, 90)
enemy3 = Enemy(-90, s_height, 'triangle', 'red')
enemy3.move(-90, s_height, -90, -s_height)
coin = Sprite(-170, -150, 'circle', 'yellow')