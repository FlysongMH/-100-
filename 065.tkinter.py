import math
from tkinter import *


class PTS:
    '''定义一个"点"类'''
    def __init__(self):
        self.x = 0
        self.y = 0


def LineToDemo(MAXPTS = 20):
    points = []
    screenx = 800
    screeny = 800
    canvas = Canvas(width = screenx,height = screeny,bg = 'white')

    AspectRatio = 0.85

    xcenter = screenx / 2
    ycenter = screeny / 2
    radius = min(screenx, screeny)/2.0 - 20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter + int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius,ycenter - radius,
                       xcenter + radius,ycenter + radius)
    for i in range(MAXPTS):
        for j in range(i,MAXPTS):
            canvas.create_line(points[i].x,points[i].y,points[j].x,points[j].y)

    canvas.pack()
    mainloop()
if __name__ == '__main__':
    LineToDemo(70)