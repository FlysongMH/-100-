'''题目：打印出如下图案（菱形）:'''

def funPrint01(n=4):
    if not isinstance(n,int) or n <1:
        print('请输入一个正整数作为棱形的大小')
        return

    width = 2*n-1
    # 上半部分
    for i in range(1,n+1):
        widthi = 2*i-1
        spacewidth = n-i
        print(' '*spacewidth, '*'*widthi,' '*spacewidth)
    # 下半部分
    for i in range(n-1, 0, -1):
        widthi = 2*i-1
        spacewidth = n-i
        print(' '*spacewidth, '*'*widthi,' '*spacewidth)


if __name__ == '__main__':
    # funPrint01(6)
    funPrint01()

