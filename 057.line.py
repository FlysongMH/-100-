'''题目：画图，学用line画直线。'''

from tkinter import *

def fun01():

    windowwidth = 800
    windowheight = 800
    top = Tk()  # 创建顶层窗口
    canvas = Canvas(top, width=windowwidth, height=windowheight, bg='yellow') # 创建控件
    canvas.pack(expand=YES, fill=BOTH)  # 放入根

    lineNum = 20
    boderdiff = 50
    lineDiff = min(windowwidth-boderdiff, windowheight-boderdiff)/2 /(lineNum+1)
    print(lineDiff)

    # 画竖线
    x0 = boderdiff
    y0 = x0
    x1 = windowwidth-x0
    y1 = windowheight-y0
    for i in range(lineNum):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='red') # 画竖线
        canvas.create_line(x1, y0, x1, y1, width=1, fill='red')
        canvas.create_line(x0, y0, x1, y0, width=1, fill='blue') # 画横线
        canvas.create_line(x0, y1, x1, y1, width=1, fill='blue')
        x0 += lineDiff
        y0 += lineDiff
        x1 -= lineDiff
        y1 -= lineDiff

    mainloop()

def fun02():
    canvas = Canvas(width=300, height=300, bg='white')
    canvas.pack(expand=YES, fill=BOTH)
    x1, y1 = 50, 20
    x2, y2 = 100, 20
    x3, y3 = 75, 40
    x4, y4 = 75, 100
    canvas.create_line(x1, y1, x3, y3, width=3, fill='red')
    canvas.create_line(x2, y2, x3, y3, width=3, fill='red')
    canvas.create_line(x1, y1, x4, y4, width=3, fill='red')
    canvas.create_line(x2, y2, x4, y4, width=3, fill='red')
    mainloop()

def fun03():
    import turtle

    def drawline(n):
        t = turtle.Pen()
        t.color(0.3, 0.8, 0.6)  # 设置颜色，在0--1之间
        t.begin_fill()  # 开始填充颜色
        for i in range(n):  # 任意边形
            t.forward(50)
            t.left(360 / n)
        t.end_fill()  # 结束填充颜色

    drawline(5)


if __name__ == '__main__':
    fun03()