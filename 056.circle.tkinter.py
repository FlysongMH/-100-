'''题目：画图，学用circle画圆形。'''
from tkinter import * # 该方式可省略调用模块时的tkinter.xxx()方式直接用xxx()

def fun01():
    # 指定画布颜色，创建一个根画布
    root = Tk()
    root.title('使用tkinter.Canvas模块画图形')
    cv = Canvas(root, bg='white')

    #创建一个矩形
    # cv.create_rectangle(10,10,110,110,fill = 'red')
    # cv.create_rectangle(10,10,110,110,outline = 'red')
    # cv.create_rectangle(10,10,200,150,
    #                     outline = 'red',
    #                     dash=1,
    #                     fill='green')

    cv.create_oval(10,10,200,110,outline = 'red')

    cv.pack()

    root.mainloop()

def fun02():
    theWidth  = 800
    theHeight = 600
    canvas = Canvas(width=theWidth, height=theHeight, bg='grey')
    canvas.pack(expand=YES, fill=BOTH)

    r=1
    while r <= min(theHeight/2, theWidth/2):
        canvas.create_oval(theWidth/2 - r, theHeight/2 - r, theWidth/2 + r, theHeight/2 + r,
                           outline = 'red',
                           width=1)
        r +=10
    mainloop()

if __name__ == '__main__':
    fun02()