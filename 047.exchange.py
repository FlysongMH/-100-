'''题目：两个变量值互换。'''


def exchange01(x,y):
    x,y = y,x   # 同一行的赋值是“并列”的，同时赋值，没有先后，不需要中间变量存储
    return (x,y)

if __name__ == '__main__':
    x,y=10,20
    print('x=%d, y=%d.'%(x,y))
    x,y=exchange01(x,y)
    print('x=%d, y=%d.'%(x,y))