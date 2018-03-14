'''题目：画图，学用rectangle画方形。　　'''
'''rectangle(int left, int top, int right, int bottom)'''

from tkinter import *

def fun01():
    windowwidth = 800
    windowheight = 800
    top = Tk()  # 创建顶层窗口
    top.title('Canvas')
    canvas = Canvas(top, width=windowwidth, height=windowheight, bg='yellow') # 创建控件
    canvas.pack(expand=YES, fill=BOTH)  # 放入根

    lineNum = 10
    boderdiff = 50
    lineDiff = min(windowwidth-boderdiff, windowheight-boderdiff)/2 /(lineNum+1)
    print(lineDiff)

    # 画方框
    x0 = boderdiff
    y0 = x0
    x1 = windowwidth-x0
    y1 = windowheight-y0
    for i in range(lineNum):
        canvas.create_rectangle(x0, y0, x1, y1, width=2)
        x0 += lineDiff
        y0 += lineDiff
        x1 -= lineDiff
        y1 -= lineDiff

    mainloop()

if __name__ == '__main__':
    fun01()