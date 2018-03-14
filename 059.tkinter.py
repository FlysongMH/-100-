'''题目：画图，综合例子。'''

from tkinter import *
import math

def fun01():
    windowwidth = 800
    windowheight = 600
    canvas = Canvas(width=windowwidth, height=windowheight, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)

    x0 = windowwidth/2
    y0 = windowheight/2

    R = min(windowheight,windowwidth)/3
    r = R/2
    # 画一个椭圆，指定左边界，上边界，右边界，下边界
    canvas.create_oval(x0 - R, y0 - R, x0 + R, y0 + R, width=2)# 画一个圆，
    canvas.create_oval(x0 - R, y0 - r, x0 + R, y0 + r, width=2)# 椭圆即是圆的拓展
    # 画一段椭圆弧，圆弧也是椭圆的拓展，只要额外再指定起始的角度度数即可。
    canvas.create_arc(x0 - R, y0 - r, x0 + R, y0 + r, start=-30, extent=60, width=1, fill='red')#从-30度开始持续60度角
    canvas.create_arc(x0 - R, y0 - r, x0 + R, y0 + r, start=150, extent=60, width=1, fill='red')
    # 画多边形，直接指定各个顶点即可。
    canvas.create_polygon(x0-R,x0+R, x0+R, x0+R, x0,x0+r, width=2, fill='blue')# 画一个三角形，三个顶点


    # 画放射线
    B = 0.809
    for i in range(10000):
        a = 2 * math.pi / 10000 * i
        x = math.ceil(x0 + r * math.cos(a))
        y = math.ceil(y0 + r * math.sin(a) * B)
        canvas.create_line(x0, y0, x, y, fill='grey', width=1)
    canvas.create_oval(x0 - r, y0 - r*B, x0 + r, y0 + r*B, width=2)# 画一个椭圆包围放射线

    mainloop()

if __name__ == '__main__':
    fun01()